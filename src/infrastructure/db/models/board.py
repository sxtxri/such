from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.common.types import BoardId, BoardName, Description
from src.infrastructure.db.models.base import Base


class Board(Base):
    """Таблица досок."""

    __tablename__ = "boards"

    board_id: Mapped[BoardId] = mapped_column(primary_key=True)

    board_name: Mapped[BoardName] = mapped_column(String(50))
    description: Mapped[Optional[Description]] = mapped_column(Text, nullable=True)
