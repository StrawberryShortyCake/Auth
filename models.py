"""" Models for Flask Notes """

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
dbx = db.session.execute

bcrypt = Bcrypt()


class User(db.Model):
    """ Creating a User classs. """

    __tablename__ = "users"

    username = db.mapped_column(
        db.String(20),
        primary_key=True,
        unique=True
    )

    # will store hashed password
    hashed_password = db.mapped_column(
        db.String(100),
        nullable=False
    )

    email = db.mapped_column(
        db.String(50),
        nullable=False,
        unique=True
    )

    first_name = db.mapped_column(
        db.String(30),
        nullable=False
    )

    last_name = db.mapped_column(
        db.String(30),
        nullable=False
    )

    # start_register
    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        """ Register user with hashed password and return the user instance """

        hashed = bcrypt.generate_password_hash(pwd).decode('utf8')

        # creating an instance of the user with the username and hashed password
        return cls(
            username=username,
            hashed_password=hashed,
            email=email,
            first_name=first_name,
            last_name=last_name)

    # start_authenticate

    @classmethod
    def authenticate(cls, username, pwd):
        """ Calidate that the user exists and the password is correct
        Return user instance if valid; else return False.
        """

        q = db.select(cls).filter_by(username=username)
        u = dbx(q).scalar_one_or_none()

        if u and bcrypt.check_password_hash(u.hashed_password, pwd):
            return u
        else:
            return False
