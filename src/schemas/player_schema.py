from main import ma


class PlayerSchema(ma.Schema):
    class Meta:
        fields = ["player_id", "p_first_name",
                  "p_last_name", "dob", "salary", "club_id", "set_of_stats_id"]


# a single player schema
player_schema = PlayerSchema()
# multiple players schema
players_schema = PlayerSchema(many=True)
