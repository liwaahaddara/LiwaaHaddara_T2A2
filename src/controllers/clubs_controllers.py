from crypt import methods
from flask import Blueprint
from main import db
from models.clubs import Club

clubs = Blueprint('clubs', __name__, url_prefix="/clubs")


@clubs.route("/", methods=["GET"])
def get_clubs():
    # retrieve all the clubs currently in the database
    clubs_list = Club.query.all()

    return "List of Clubs"
