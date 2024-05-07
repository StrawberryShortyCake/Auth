import os

from flask import Flask, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, dbx, User
from forms import RegisterForm, LoginForm, CSRFProtectForm

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


@app.route('/register', methods=["GET", "POST"])
def display_register_user():
    """Produce register form or handle register.
    Register form accepts a username, password, email, first_name, and last_name."""

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_user = User.register(
            username=username,
            pwd=password,
            email=email,
            first_name=first_name,
            last_name=last_name)

        db.session.add(new_user)
        db.session.commit()

        session["username"] = new_user.username

        print("add a new user", new_user)

        return redirect(f"/users/{new_user.username}")

    else:
        return render_template("/user_register.jinja", form=form)


@app.route('/login', methods=["GET", "POST"])
def display_user_login():
    """ Produce login form or handle login
    This form should accept a username and a password."""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        login_user = User.authenticate(
            username=username,
            pwd=password
        )

        session["username"] = login_user.username

        print("logged in a new user", login_user)
        print("!!!!!!!!!!!!!!!SESSION", session)

        return redirect(f"/users/{login_user.username}")

    else:
        return render_template("/user_login.jinja", form=form)


@app.get("/users/<username>")
def show_user_page(username):
    """Display page that shows information about that user"""

    if "username" not in session:
        flash("Please log in!")

        return redirect("/")  # TODO: take user to the login page

    else:
        session_username = session["username"]
        q = db.select(User).where(User.username == session_username)
        user = dbx(q).scalars().one()

        return render_template("user_info.jinja", user=user)


@app.post('/logout')
def log_out_of_account():
    """Logs out of user account"""

    form = CSRFProtectForm()

    if form.validate_on_submit():
        session.pop('username', None)

    return redirect('/')
