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
def get_doctor(id):
    # retrieve a specific doctor from the database
    doctor = Doctor.query.get(id)
    # check if doctor exist in the database
    if not doctor:
        return {"error": "doctor id not found in the database"}, 404
    result = doctor_schema.dump(doctor)
    return jsonify(result)


# Adding a new Doctor to the Database
@doctors.route("/", methods=["POST"])
def new_doctor():
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


# Updating the attributes of an exisiting Doctor
@doctors.route("/<int:id>", methods=["PUT"])
def update_doctor(id):
    # find the doctor in the database
    doctor = Doctor.query.get(id)
    # check if doctor exist in the database
    if not doctor:
        return {"error": "doctor id not found in the database"}, 404
    # get the doctor details from the request
    doctor_fields = doctor_schema.load(request.json)
    # update the values of the doctor
    doctor.d_first_name = doctor_fields["d_first_name"]
    doctor.d_last_name = doctor_fields["d_last_name"]
    doctor.years_served = doctor_fields["years_served"]
    doctor.club_id = doctor_fields["club_id"]

    # save changes in the database
    db.session.commit()

    return jsonify(doctor_schema.dump(doctor)), 201


# Deleting an exisiting Doctor from the database
@doctors.route("/<int:id>", methods=["DELETE"])
def delete_doctor(id):
    # search doctor by id (primary key)
    doctor = Doctor.query.get(id)

    # check if we found a Doctor
    if not doctor:
        return {"error": "doctor_id not found"}

    # delete the doctor from the database
    db.session.delete(doctor)
    # save the changes in the database
    db.session.commit()

    return {"message": "Doctor removed successfully"}
