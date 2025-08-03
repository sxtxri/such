import datetime
from typing import Optional

from sqlalchemy import (
    BigInteger,
    Date,
    ForeignKey,
    Identity,
    Integer,
    String,
    Text,
    Time,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.common.types import AuthorNickname, PostId, PostText, ThreadId
from src.infrastructure.db.models.base import Base


class Post(Base):
    """Таблица постов."""

    __tablename__ = "posts"

    post_id: Mapped[PostId] = mapped_column(BigInteger, Identity(), primary_key=True)

    author_nickname: Mapped[Optional[AuthorNickname]] = mapped_column(String(50),
                                                                      nullable=True
                                                                      )
    post_text: Mapped[PostText] = mapped_column(Text)
    created_at_date: Mapped[datetime.date] = mapped_column(Date)
    created_at_time: Mapped[datetime.time] = mapped_column(Time)

    reply_thread: Mapped[ThreadId] = mapped_column(Integer,
                                                   ForeignKey("threads.thread_id"))
    reply_post: Mapped[Optional[PostId]] = mapped_column(Integer, nullable=True)
