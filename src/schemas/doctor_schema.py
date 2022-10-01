from main import ma


class DoctorSchema(ma.Schema):
    class Meta:
        fields = ["doctor_id", "d_first_name",
                  "d_last_name", "years_served", "club_id"]


# a single doctor schema
doctor_schema = DoctorSchema()
# multiple doctors schema
doctors_schema = DoctorSchema(many=True)
