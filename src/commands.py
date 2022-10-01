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


# @db.cli.command('seed')
# def seed_db():

#     # Create a new Card (in memory)
#     card = Card(
#         title="Start the project",
#         description="Stage 1 - create db",
#         status="To Do",
#         priority="High",
#         date=date.today()
#     )

#     # Add the new card to the current transaction (in memory)
#     db.session.add(card)

#     admin = User(
#         email="admin@email.com",
#         # password = "12345678",
#         password=bcrypt.generate_password_hash("12345678").decode("utf-8"),
#         admin=True
#     )

#     db.session.add(admin)

#     # Commit the transaction to the physical DB
#     db.session.commit()

#     print('Table seeded')
