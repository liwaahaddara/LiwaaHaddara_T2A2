from main import ma


class ClubSchema(ma.Schema):
    class Meta:
        fields = ["club_id", "club_name", "city_located", "year_established"]


# a single club schema
club_schema = ClubSchema()

# multiple clubs schema
clubs_schema = ClubSchema(many=True)
