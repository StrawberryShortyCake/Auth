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

    notes = db.relationship(
        "Note",
        back_populates="owner",
        cascade="all, delete-orphan"
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
        """ Validate that the user exists and the password is correct
        Return user instance if valid; else return False.
        """

        q = db.select(cls).filter_by(username=username)
        # can't use get or 404, db.session.get => use user instead
        u = dbx(q).scalar_one_or_none()

        if u and bcrypt.check_password_hash(u.hashed_password, pwd):
            return u
        else:
            return False


class Note(db.Model):
    """ Creating a Note Class """

    __tablename__ = "notes"

    id = db.mapped_column(
        db.Integer,
        db.Identity(),
        primary_key=True
    )

    title = db.mapped_column(
        db.String(100),
        nullable=False
    )

    content = db.mapped_column(
        db.Text,
        nullable=False
    )

    owner_username = db.mapped_column(
        db.String(20),
        db.ForeignKey('users.username', ondelete="CASCADE",
                      onupdate="CASCADE"),
        nullable=False
    )

    owner = db.relationship(
        "User",
        back_populates="notes"
    )
