from main import db


class Doctor(db.Model):
    # defining the tablename in the database as 'doctors'
    __tablename__ = "doctors"

    # setting the attributes of the Doctor Entity
    doctor_id = db.Column(db.Integer, primary_key=True)
    d_first_name = db.Column(db.String())
    d_last_name = db.Column(db.String())
    years_served = db.Column(db.Integer)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.club_id"))
