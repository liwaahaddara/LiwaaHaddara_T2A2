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
    stat = Stat.query.get(id)
    # check if stat exist in the database
    if not stat:
        return {"error": "stat id not found in the database"}, 404
    result = stat_schema.dump(stat)
    return jsonify(result)


# Adding a new Stats entry to the Database
@stats.route("/", methods=["POST"])
def new_stat():
    stat_fields = stat_schema.load(request.json)
    stat = Stat(
        games_played=stat_fields["games_played"],
        goals=stat_fields["goals"],
        position=stat_fields["position"],
        avg_disposals=stat_fields["avg_disposals"],
        avg_tackles=stat_fields["avg_tackles"],
        avg_marks=stat_fields["avg_marks"],
        player_id=stat_fields["player_id"]
    )

    db.session.add(stat)
    db.session.commit()

    return jsonify(stat_schema.dump(stat))


# Updating the attributes of an exisiting player's Stats
@stats.route("/<int:id>", methods=["PUT"])
def update_stat(id):
    # find the stat in the database
    stat = Stat.query.get(id)
    # check if stat exist in the database
    if not stat:
        return {"error": "stat id not found in the database"}, 404
    # get the stat details from the request
    stat_fields = stat_schema.load(request.json)
    # update the values of the stat
    stat.games_played = stat_fields["games_played"]
    stat.goals = stat_fields["goals"]
    stat.position = stat_fields["position"]
    stat.avg_disposals = stat_fields["avg_disposals"]
    stat.avg_tackles = stat_fields["avg_tackles"]
    stat.avg_marks = stat_fields["avg_marks"]
    stat.player_id = stat_fields["player_id"]

    # save changes in the database
    db.session.commit()

    return jsonify(stat_schema.dump(stat)), 201


# Deleting an exisiting Player's stats from the database
@stats.route("/<int:id>", methods=["DELETE"])
def delete_stat(id):
    # search stat by id (primary key)
    stat = Stat.query.get(id)

    # check if we found a Player's stats
    if not stat:
        return {"error": "stat_id not found"}

    # delete the player's stats from the database
    db.session.delete(stat)
    # save the changes in the database
    db.session.commit()

    return {"message": "Stat removed successfully"}
