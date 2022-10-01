from main import db


class Stat(db.Model):
    # defining the tablename in the database as 'stats'
    __tablename__ = "stats"

    # setting the attributes of the Stat Entity
    set_of_stats_id = db.Column(db.Integer, primary_key=True)
    games_played = db.Column(db.Integer)
    goals = db.Column(db.Integer)
    position = db.Column(db.String())
    avg_disposals = db.Column(db.Integer)
    avg_tackles = db.Column(db.Integer)
    avg_marks = db.Column(db.Integer)
