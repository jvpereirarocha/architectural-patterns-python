from uuid import uuid4
from dataclasses import dataclass, field
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    # Necessary to prevent circular imports
    from app.domain.vote_repository import VoteRepository


@dataclass
class Vote:
    vote_id: str = field(default_factory=lambda: str(uuid4()))

    def save_vote(self, vote_repo: 'VoteRepository'):
        return vote_repo.add(self)
    
    def __hash__(self) -> int:
        return hash(self.vote_id)