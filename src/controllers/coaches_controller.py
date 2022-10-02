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
    return jsonify(result), 200


@coaches.route("/<int:id>", methods=["GET"])
def get_coach(id):
    # retrieve a specific coach from the database
    coach = Coach.query.get(id)
    # check if coach exist in the database
    if not coach:
        return {"error": "coach id not found in the database"}, 404
    result = coach_schema.dump(coach)
    return jsonify(result), 200


# Adding a new Coach to the Database
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

    return jsonify(coach_schema.dump(coach)), 200


# Updating the attributes of an exisiting Coach
@coaches.route("/<int:id>", methods=["PUT"])
def update_coach(id):
    # find the coach in the database
    coach = Coach.query.get(id)
    # check if coach exist in the database
    if not coach:
        return {"error": "coach id not found in the database"}, 404
    # get the coach details from the request
    coach_fields = coach_schema.load(request.json)
    # update the values of the coach
    coach.c_first_name = coach_fields["c_first_name"]
    coach.c_last_name = coach_fields["c_last_name"]
    coach.coach_type = coach_fields["coach_type"]
    coach.years_coached = coach_fields["years_coached"]
    coach.club_id = coach_fields["club_id"]

    # save changes in the database
    db.session.commit()

    return jsonify(coach_schema.dump(coach)), 201


# Deleting an exisiting Coach from the database
@coaches.route("/<int:id>", methods=["DELETE"])
def delete_coach(id):
    # search coach by id (primary key)
    coach = Coach.query.get(id)

    # check if we found a Coach
    if not coach:
        return {"error": "coach_id not found"}

    # delete the coach from the database
    db.session.delete(coach)
    # save the changes in the database
    db.session.commit()

    return {"message": "Coach removed successfully"}
