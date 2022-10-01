from main import db


class Club(db.Model):
    # defining the tablename in the database as 'clubs'
    __tablename__ = "clubs"

    # setting the attributes of the Club Entity
    club_id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String())
    city_located = db.Column(db.String())
    year_established = db.Column(db.Integer)
