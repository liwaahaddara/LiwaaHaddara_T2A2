from main import ma


class CoachSchema(ma.Schema):
    class Meta:
        fields = ["coach_id", "c_first_name", "c_last_name",
                  "coach_type", "years_coached", "club_id"]


# a single coach schema
coach_schema = CoachSchema()
# multiple coaches schema
coaches_schema = CoachSchema(many=True)
