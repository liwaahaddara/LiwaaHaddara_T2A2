from main import db


class Coach(db.Model):
    # defining the tablename in the database as 'coaches'
    __tablename__ = "coaches"

    # setting the attributes of the Coach Entity
    coach_id = db.Column(db.Integer, primary_key=True)
    c_first_name = db.Column(db.String())
    c_last_name = db.Column(db.String())
    coach_type = db.Column(db.String())
    years_coached = db.Column(db.Integer)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.club_id"))
