from abc import ABC, abstractmethod
from typing import Iterable

from app.domain.vote import Vote


class VoteRepository(ABC):
    @abstractmethod
    def add(self, vote: Vote) -> Vote:
        raise NotImplementedError()
    
    @abstractmethod
    def get_all(self) -> Iterable[Vote]:
        raise NotImplementedError()
    
    @abstractmethod
    def total_of_votes(self) -> int:
        raise NotImplementedError()