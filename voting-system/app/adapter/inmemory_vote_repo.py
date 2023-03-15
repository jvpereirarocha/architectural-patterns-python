from typing import Iterable

from app.domain.vote import Vote
from app.domain.vote_repository import VoteRepository


class InMemoryVoteRepository(VoteRepository):
    def __init__(self):
        self.votes = set()

    def add(self, vote: Vote) -> Vote:
        self.votes.add(vote)
        return vote
    
    def get_all(self) -> Iterable[Vote]:
        return self.votes
    
    def total_of_votes(self) -> int:
        return len(self.votes)