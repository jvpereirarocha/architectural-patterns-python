from flask import Blueprint, jsonify
from app.domain.vote import Vote
from app.adapter.inmemory_vote_repo import InMemoryVoteRepository


votes = Blueprint("votes", __name__, url_prefix="/votes")


repo = InMemoryVoteRepository()

@votes.route("/", methods=["GET"])
def get_total_of_votes():
    total = repo.total_of_votes()
    message = {"message": f"Total of votes: {total}"}
    return jsonify(message), 200


@votes.route("/add", methods=["POST"])
def add_new_vote():
    new_vote = Vote()
    new_vote.save_vote(vote_repo=repo)
    return jsonify({"message": "New vote added"}), 201