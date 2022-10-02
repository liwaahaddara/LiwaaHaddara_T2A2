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
    return jsonify(result), 200


@players.route("/<int:id>", methods=["GET"])
def get_player(id):
    # retrieve a specific player from the database
    player = Player.query.get(id)
    # check if player exist in the database
    if not player:
        return {"error": "player id not found in the database"}, 404
    result = player_schema.dump(player)
    return jsonify(result), 200


# Adding a new Player to the Database
@players.route("/", methods=["POST"])
def new_player():
    player_fields = player_schema.load(request.json)
    player = Player(
        p_first_name=player_fields["p_first_name"],
        p_last_name=player_fields["p_last_name"],
        p_dob=player_fields["p_dob"],
        p_salary=player_fields["p_salary"],
        club_id=player_fields["club_id"]
    )

    db.session.add(player)
    db.session.commit()

    return jsonify(player_schema.dump(player)), 200


# Updating the attributes of an exisiting Player
@players.route("/<int:id>", methods=["PUT"])
def update_player(id):
    # find the player in the database
    player = Player.query.get(id)
    # check if player exist in the database
    if not player:
        return {"error": "player id not found in the database"}, 404
    # get the player details from the request
    player_fields = player_schema.load(request.json)
    # update the values of the player
    player.p_first_name = player_fields["p_first_name"]
    player.p_last_name = player_fields["p_last_name"]
    player.p_dob = player_fields["p_dob"]
    player.p_salary = player_fields["p_salary"]
    player.club_id = player_fields["club_id"]

    # save changes in the database
    db.session.commit()

    return jsonify(player_schema.dump(player)), 201


# Deleting an exisiting Player from the database
@players.route("/<int:id>", methods=["DELETE"])
def delete_player(id):
    # search player by id (primary key)
    player = Player.query.get(id)

    # check if we found a Player
    if not player:
        return {"error": "player_id not found"}

    # delete the player from the database
    db.session.delete(player)
    # save the changes in the database
    db.session.commit()

    return {"message": "Player removed successfully"}
