from flask import Blueprint
from main import db
from models.clubs import Club
from models.coaches import Coach
from models.doctors import Doctor
from models.players import Player
from models.stats import Stat


db_commands = Blueprint("db", __name__)


@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all AFL models in the physical DB
    db.create_all()
    print('Tables created')


@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables
    db.drop_all()
    print('Tables dropped')


@db_commands.cli.command('seed')
def seed_db():
    # Create a new Club entry (in memory)
    club1 = Club(
        club_name="Western Bulldogs",
        city_located="Melbourne",
        year_established=1877
    )

    # Add the new club to the current transaction (in memory)
    db.session.add(club1)

    # Commit the transaction to the physical DB
    db.session.commit()

    print('Table seeded')
