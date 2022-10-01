from flask import Blueprint, jsonify, request
from main import db
from models.coaches import Coach
from schemas.coach_schema import coach_schema, coaches_schema


coaches = Blueprint('coaches', __name__, url_prefix="/coaches")


@coaches.route("/", methods=["GET"])
def get_coaches():
    # retrieve all the coaches currently in the database
    coaches_list = Coach.query.all()
    result = coaches_schema.dump(coaches_list)
    return jsonify(result)


@coaches.route("/<int:id>", methods=["GET"])
def get_coach(id):
    # retrieve a specific coach from the database
    coach = Coach.query.get(id)
    result = coach_schema.dump(coach)
    return jsonify(result)


@coaches.route("/", methods=["POST"])
def new_coach():
    coach_fields = coach_schema.load(request.json)
    coach = Coach(
        c_first_name=coach_fields["c_first_name"],
        c_last_name=coach_fields["c_last_name"],
        coach_type=coach_fields["coach_type"],
        years_coached=coach_fields["years_coached"],
        club_id=coach_fields["club_id"]
    )

    db.session.add(coach)
    db.session.commit()

    return jsonify(coach_schema.dump(coach))
