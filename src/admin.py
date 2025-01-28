# ruff: noqa: F401
# Import admin directory which was used to create admin views to register them

import src.hero.admin
from src.common.admin import AdminManager

admin = AdminManager()
