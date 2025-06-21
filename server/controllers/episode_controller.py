from flask import Blueprint, jsonify, abort
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance

episode_bp = Blueprint("episode", __name__)

@episode_bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.order_by(Episode.date.desc()).all()
    result = [{
        "id": ep.id,
        "date": ep.date.isoformat(),
        "number": ep.number
    } for ep in episodes]
    return jsonify(result), 200

@episode_bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    ep = Episode.query.get_or_404(id)
    appearances = [{
        "id": a.id,
        "rating": a.rating,
        "guest_id": a.guest_id
    } for a in ep.appearances]
    return jsonify({
        "id": ep.id,
        "date": ep.date.isoformat(),
        "number": ep.number,
        "appearances": appearances
    }), 200

@episode_bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get_or_404(id)
    # Delete cascade should delete appearances
    from server.app import db
    db.session.delete(ep)
    db.session.commit()
    return jsonify({"message": f"Episode {id} deleted"}), 200
