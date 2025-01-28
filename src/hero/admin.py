from sqladmin import ModelView

from src.common.admin import AdminManager

from src.hero import models

admin_manager = AdminManager()


@admin_manager.register
class HeroAdmin(ModelView, model=models.Hero):
    column_display = ("id", "name")
