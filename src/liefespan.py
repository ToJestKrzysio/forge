from fastapi import FastAPI

from src.common.utils.validate_subclasses_mixin import ValidateSubclassesMixin


async def startup(_app: FastAPI):
    ValidateSubclassesMixin.validate_subclasses()


async def teardown(_app: FastAPI):
    return
