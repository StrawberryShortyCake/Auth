import os

from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, dbx, User
# from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///flask_notes')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db.init_app(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"


@app.get('/')
def redirect_register():
    """Redirects from / to /register"""

    return redirect('/register')


@app.get('/register')
def display_register_user():
    """Show form that will register/create a user.
    This form accepts a username, password, email, first_name, and last_name."""
