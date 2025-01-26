from unittest.mock import patch

import pytest
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings

from src.common.utils.validate_subclasses_mixin import ValidateSubclassesMixin


@pytest.mark.parametrize(
    "env_vars, expected_error",
    [
        [{"BAR": "bar", "BAZ": "baz"}, "1 validation error for A\nFOO\n  Field required"],
        [{"FOO": "foo", "BAZ": "baz"}, "1 validation error for B\nBAR\n  Field required"],
        [{"FOO": "foo", "BAR": "bar"}, "1 validation error for D\nBAZ\n  Field required"],
    ],
    ids=["FOO", "BAR", "BAZ"],
)
def test_validate_settings_on_startup_mixin(env_vars: dict, expected_error: str, monkeypatch):
    for key, value in env_vars.items():
        monkeypatch.setenv(key, value)

    class A(BaseSettings, ValidateSubclassesMixin):
        foo: str = Field(validation_alias="FOO")

    class B(BaseSettings, ValidateSubclassesMixin):
        bar: str = Field(validation_alias="BAR")

    class C(BaseSettings, ValidateSubclassesMixin):
        pass

    class D(C):
        baz: str = Field(validation_alias="BAZ")

    with (
        patch.object(ValidateSubclassesMixin, "__subclasses__", return_value=[A, B, C]),
        patch.object(A, "__subclasses__", return_value=[A]),
        patch.object(B, "__subclasses__", return_value=[B]),
        patch.object(C, "__subclasses__", return_value=[C, D]),
        patch.object(D, "__subclasses__", return_value=[D]),
    ):
        with pytest.raises(ValidationError, match=expected_error):
            ValidateSubclassesMixin.validate_subclasses()
