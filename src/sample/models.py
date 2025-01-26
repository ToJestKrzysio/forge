from sqlalchemy.orm import Mapped, mapped_column

from src.common.database import Base


class Hero(Base):
    __tablename__ = "hero"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
