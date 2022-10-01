from flask import Blueprint, jsonify, request
from main import db
from models.players import Player
from schemas.player_schema import player_schema, players_schema


players = Blueprint('players', __name__, url_prefix="/players")


@players.route("/", methods=["GET"])
def get_players():
    # retrieve all the players currently in the database
    players_list = Player.query.all()
    result = players_schema.dump(players_list)
    return jsonify(result)


@players.route("/<int:id>", methods=["GET"])
def get_player(id):
    # retrieve a specific player from the database
    player = player.query.get(id)
    result = player_schema.dump(player)
    return jsonify(result)


@players.route("/", methods=["POST"])
def new_player():
    player_fields = player_schema.load(request.json)
    player = Player(
        p_first_name=player_fields["p_first_name"],
        p_last_name=player_fields["p_last_name"],
        p_dob=player_fields["p_dob"],
        p_salary=player_fields["p_salary"],
        club_id=player_fields["club_id"],
        set_of_stats_id=player_fields["set_of_stats_id"]
    )

    db.session.add(player)
    db.session.commit()

    return jsonify(player_schema.dump(player))
