import datetime
from typing import NamedTuple

type BoardId = int
type BoardName = str
type Description = str

type ThreadId = int
type ThreadName = str

type PostId = int
type AuthorNickname = str
type PostText = str


class Post(NamedTuple):
    post_id = PostId
    author_nickname = AuthorNickname | None
    post_text = PostText
    created_at_date = datetime.date
    created_at_time = datetime.time
    reply_thread = ThreadId
    reply_post = PostId | None