from sqlalchemy.orm import Mapped, mapped_column

from src.common.database import Base


class Hero(Base):  # TODO REMOVE FILE
    __tablename__ = "hero"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"
