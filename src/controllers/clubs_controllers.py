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


@clubs.route("/<int:id>", methods=["GET"])
def get_club(id):
    # retrieve a specific club from the database
    club = Club.query.get(id)
    result = club_schema.dump(club)
    return jsonify(result)


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
