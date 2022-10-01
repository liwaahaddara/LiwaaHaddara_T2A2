from flask import Blueprint, jsonify, request
from main import db
from models.doctors import Doctor
from schemas.doctor_schema import doctor_schema, doctors_schema


doctors = Blueprint('doctors', __name__, url_prefix="/doctors")


@doctors.route("/", methods=["GET"])
def get_doctors():
    # retrieve all the doctors currently in the database
    doctors_list = Doctor.query.all()
    result = doctors_schema.dump(doctors_list)
    return jsonify(result)


@doctors.route("/<int:id>", methods=["GET"])
def get_coach(id):
    # retrieve a specific doctor from the database
    doctor = doctor.query.get(id)
    result = doctor_schema.dump(doctor)
    return jsonify(result)


@doctors.route("/", methods=["POST"])
def new_club():
    doctor_fields = doctor_schema.load(request.json)
    doctor = Doctor(
        d_first_name=doctor_fields["c_first_name"],
        d_last_name=doctor_fields["c_last_name"],
        years_served=doctor_fields["years_served"],
        club_id=doctor_fields["club_id"]
    )

    db.session.add(doctor)
    db.session.commit()

    return jsonify(doctor_schema.dump(doctor))
