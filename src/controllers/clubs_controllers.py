from crypt import methods
from flask import Blueprint, jsonify
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
