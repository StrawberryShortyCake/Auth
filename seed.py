"""Seed playlist_app db with data."""

from app import app
from models import db, dbx, User

app.app_context().push()

db.drop_all()
db.create_all()

user1 = User.register(
    username="testuser1",
    pwd='password1',
    email='hello1@yahoo.com',
    first_name='Patrick',
    last_name="Starr"
)

user2 = User.register(
    username="testuser2",
    pwd='password2',
    email='hello2@yahoo.com',
    first_name='Spongebob',
    last_name="Squarepants"
)

db.session.add_all([user1, user2])

db.session.commit()
