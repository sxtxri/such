import datetime

from sqlalchemy import (
    Date,
    ForeignKey,
    Integer,
    String,
    Time,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import Base


class Thread(Base):
    """Таблица тредов."""

    __tablename__ = "threads"

    thread_id: Mapped[int] = mapped_column(primary_key=True)

    thread_name: Mapped[str] = mapped_column(String(50))
    created_at_date: Mapped[datetime.date] = mapped_column(Date)
    created_at_time: Mapped[datetime.time] = mapped_column(Time)
    updated_at_date: Mapped[datetime.date] = mapped_column(Date)
    updated_at_time: Mapped[datetime.time] = mapped_column(Time)

    reply_board: Mapped[int] = mapped_column(Integer,
                                             ForeignKey("boards.board_id"))
