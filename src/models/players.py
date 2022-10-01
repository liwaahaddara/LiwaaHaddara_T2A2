from main import db


class Player(db.Model):
    # defining the tablename in the database as 'players'
    __tablename__ = "players"

    # setting the attributes of the Player Entity
    player_id = db.Column(db.Integer, primary_key=True)
    p_first_name = db.Column(db.String())
    p_last_name = db.Column(db.String())
    p_dob = db.Column(db.Date())
    p_salary = db.Column(db.Integer)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.club_id"))
    statsFK = db.relationship(
        "Stat",
        backref="players"
    )
