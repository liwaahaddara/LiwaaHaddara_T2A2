from flask import Blueprint, jsonify, request
from main import db
from models.clubs import Club
from schemas.club_schema import club_schema, clubs_schema


clubs = Blueprint('clubs', __name__, url_prefix="/clubs")


@clubs.route("/", methods=["GET"])
def get_clubs():
    # retrieve all the clubs currently in the database
    clubs_list = Club.query.all()
    result = clubs_schema.dump(clubs_list)
    return jsonify(result)


# Searching for a single, exisiting club in the database
@clubs.route("/<int:id>", methods=["GET"])
def get_club(id):
    # retrieve a specific club from the database
    club = Club.query.get(id)
    # check if club exist in the database
    if not club:
        return {"error": "club id not found in the database"}, 404
    result = club_schema.dump(club)
    return jsonify(result)


# Adding a new Club to the Database
@clubs.route("/", methods=["POST"])
def new_club():
    club_fields = club_schema.load(request.json)
    club = Club(
        club_name=club_fields["club_name"],
        city_located=club_fields["city_located"],
        year_established=club_fields["year_established"]
    )

    db.session.add(club)
    db.session.commit()

    return jsonify(club_schema.dump(club))


# Updating the attributes of an exisiting Club
@clubs.route("/<int:id>", methods=["PUT"])
def update_club(id):
    # find the club in the database
    club = Club.query.get(id)
    # check if club exist in the database
    if not club:
        return {"error": "club id not found in the database"}, 404
    # get the club details from the request
    club_fields = club_schema.load(request.json)
    # update the values of the club
    club.club_name = club_fields["club_name"]
    club.city_located = club_fields["city_located"]
    club.year_established = club_fields["year_established"]

    # save changes in the database
    db.session.commit()

    return jsonify(club_schema.dump(club)), 201


# Deleting an exisiting Club from the database
@clubs.route("/<int:id>", methods=["DELETE"])
def delete_club(id):
    # search club by id (primary key)
    club = Club.query.get(id)

    # check if we found a Club
    if not club:
        return {"error": "club_id not found"}

    # delete the club from the database
    db.session.delete(club)
    # save the changes in the database
    db.session.commit()

    return {"message": "Club removed successfully"}
