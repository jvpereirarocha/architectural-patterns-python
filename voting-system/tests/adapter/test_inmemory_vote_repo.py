from app.adapter.inmemory_vote_repo import InMemoryVoteRepository
from app.domain.vote import Vote


def test_vote_save():
    vote = Vote()
    repo = InMemoryVoteRepository()
    assert vote.save_vote(vote_repo=repo).vote_id == vote.vote_id


def test_vote_repository_all():
    repo = InMemoryVoteRepository()
    first_vote = Vote()
    second_vote = Vote()

    first_vote.save_vote(vote_repo=repo)
    second_vote.save_vote(vote_repo=repo)

    assert repo.get_all() == set([first_vote, second_vote])


def test_vote_repo_total():
    repo = InMemoryVoteRepository()
    
    Vote().save_vote(vote_repo=repo)
    Vote().save_vote(vote_repo=repo)
    Vote().save_vote(vote_repo=repo)

    assert repo.total_of_votes() == 3