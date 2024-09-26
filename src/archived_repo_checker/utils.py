from dataclasses import dataclass
from typing import Optional

import httpx

@dataclass
class Result:
    confirmed: bool
    """ is the result reliable """
    repo_deleted: bool
    repo_archived: bool
    repo_real: str
    """ the real URL after redirects """
    error: Optional[Exception]
    def __init__(
        self,
        *,
        confirmed: bool = False,
        repo_deleted: bool = False,
        repo_archived: bool = False,
        real_src: str = "",
        error: Optional[Exception] = None,
    ):
        self.confirmed = confirmed
        self.repo_deleted = repo_deleted
        self.repo_archived = repo_archived
        self.repo_real = real_src
        self.error = error


global_client = httpx.Client(
    http2=True,
    headers={
        "User-Agent": "is_archived_repo/0.1.0 (is_archived_repo checker)",
        "language": "en-US,en;q=0.5",
    },
    timeout=5,
)
