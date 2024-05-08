"""Seed playlist_app db with data."""

from app import app
from models import db, dbx, User, Note

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


user1_note1 = Note(
    title="Hey this is a title",
    content="blah blah blaaaaaaaah",
    owner_username="testuser1"
)

user1_note2 = Note(
    title="Another one",
    content="DJ KHALED",
    owner_username="testuser1"
)

user1_note3 = Note(
    title="Brady is not a goat",
    content="baaaaaaah",
    owner_username="testuser1"
)

user2_note1 = Note(
    title="Ben Afleck is not funny",
    content="He should quit Twitter",
    owner_username="testuser2"
)

db.session.add_all([user1_note1, user1_note2, user1_note3, user2_note1])
db.session.commit()
