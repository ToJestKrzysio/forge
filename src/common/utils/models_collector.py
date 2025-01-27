import sys
from inspect import getmembers, isclass
import logging
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
from typing import Generator

from sqlalchemy.orm import DeclarativeBase
from src.common.base_model import BaseModel  # noqa

logger = logging.getLogger(__name__)


class ModelsCollector:
    """Utility used to dynamically import all SQL alchemy ORM models in specified location."""

    EXCLUDED_FILES = {"__init__"}

    def __init__(self, path: Path | str):
        """

        :param path: Root path from which search will begin
        """
        self.path = Path(path)
        if not self.path.exists():
            raise FileNotFoundError(f"Path {self.path} not found.")

    def collect_models(self) -> list[type[DeclarativeBase]]:
        """Perform collection of classes in specified location."""
        collected = []
        for file in self._get_valid_python_files():
            collected.extend(self._load_classes_from_file(file))
        return collected

    def _get_valid_python_files(self) -> Generator[Path, None, None]:
        """Search for all python files in specified location, excluding EXCLUDED_FILES"""
        for file in self.path.rglob("*.py"):
            if file.stem in self.EXCLUDED_FILES:
                logger.debug(f"ModelsCollector._get_valid_python_files - Skipping excluded file: {file.stem}")
                continue
            yield file

    def _load_classes_from_file(self, file: Path) -> list[type[DeclarativeBase]]:
        """Load all classes from specified file"""
        module_path = file.relative_to(self.path.parent).with_suffix("")
        module_name = str(module_path).replace("/", ".")

        spec = spec_from_file_location(module_name, file.absolute())
        if spec is None or spec.loader is None:
            logger.error(f"ModelsCollector._load_classes_from_file - Could not load spec for file: {file.stem}")
            return []

        if module_name not in sys.modules:
            logger.debug(f"ModelsCollector._load_classes_from_file - Loading module: {module_name}")
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            logger.debug(f"ModelsCollector._load_classes_from_file - Module already loaded: {module_name}")
            module = sys.modules[module_name]

        classes = []
        for name, cls in getmembers(module, isclass):
            if cls.__module__ != module_name:
                logger.debug(f"ModelsCollector._load_classes_from_file - External class: {module_name}")
                continue
            classes.append(cls)

        return [cls for cls in classes if issubclass(cls, DeclarativeBase)]
