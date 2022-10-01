from turtle import st
from flask import Blueprint, jsonify, request
from main import db
from models.stats import Stat
from schemas.stat_schema import stat_schema, stats_schema


stats = Blueprint('stats', __name__, url_prefix="/stats")


@stats.route("/", methods=["GET"])
def get_stats():
    # retrieve all the stats currently in the database
    stats_list = Stat.query.all()
    result = stats_schema.dump(stats_list)
    return jsonify(result)


@stats.route("/<int:id>", methods=["GET"])
def get_stat(id):
    # retrieve a specific stat from the database
    stat = stat.query.get(id)
    result = stat_schema.dump(stat)
    return jsonify(result)


@stats.route("/", methods=["POST"])
def new_stat():
    stat_fields = stat_schema.load(request.json)
    stat = Stat(
        set_of_stats_id=stat_fields["set_of_stats_id"],
        games_played=stat_fields["games_played"],
        goals=stat_fields["goals"],
        position=stat_fields["position"],
        avg_disposals=stat_fields["avg_disposals"],
        avg_tackles=stat_fields["avg_tackles"],
        avg_marks=stat_fields["avg_marks"]
    )

    db.session.add(stat)
    db.session.commit()

    return jsonify(stat_schema.dump(stat))
