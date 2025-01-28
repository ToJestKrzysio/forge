from sqladmin import ModelView, BaseView, Admin
from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncEngine
from starlette.applications import Starlette


class AdminManager:
    _shared_dict = {"views": set()}

    def __init__(self):
        self.__dict__ = self._shared_dict

    @property
    def views(self) -> set[type[ModelView | BaseView]]:
        return self.__dict__["views"]

    def register(self, view: type[ModelView | BaseView]) -> None:
        self.views.add(view)

    def build(self, app: Starlette, engine: Engine | AsyncEngine) -> Admin:
        admin = Admin(app=app, engine=engine)
        for view in self.views:
            admin.add_view(view)

        return admin
