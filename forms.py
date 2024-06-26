from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField
from wtforms.validators import InputRequired, Length


class RegisterForm(FlaskForm):
    """Form for registering user"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(max=20)]
    )

    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8, max=20)]
    )

    email = EmailField(
        "Email",
        validators=[InputRequired(), Length(max=50)]
    )

    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)]
    )

    last_name = StringField(
        'Last Name',
        validators=[InputRequired(), Length(max=30)]
    )


class LoginForm(FlaskForm):
    """Form for logging in"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(max=20)]
    )

    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8, max=20)]
    )


class CSRFProtectForm(FlaskForm):
    """Form for CSRF protection"""


class AddNoteForm(FlaskForm):
    """Form for adding note"""

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=100)]
    )

    content = TextAreaField(
        "Content",
        validators=[InputRequired()]
    )
