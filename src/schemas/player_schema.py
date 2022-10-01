from main import ma


class PlayerSchema(ma.Schema):
    class Meta:
        fields = ["player_id", "p_first_name",
                  "p_last_name", "p_dob", "p_salary", "club_id"]


# a single player schema
player_schema = PlayerSchema()
# multiple players schema
players_schema = PlayerSchema(many=True)
