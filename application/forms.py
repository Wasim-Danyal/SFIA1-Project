
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import current_user


class RegistrationForm(FlaskForm):
    first_name = StringField('Forename',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    last_name = StringField('Surname',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )
    email = StringField('Email Address',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Please confirm your password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Sorry, that E-Mail is already in use, please try another')


class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		]
    )
	password = PasswordField('Password',
		validators=[
			DataRequired(),
		]
    )
	remember = BooleanField('Remember Me')
    
	submit = SubmitField('Login')

class NewRate(FlaskForm):
    base_currency = StringField('Base Currency',
    validators=[
        DataRequired(),
        Length(min=3, max=3)
        ]
    )
    new_currency = StringField('Pair Currency',
    validators=[
        DataRequired(),
        Length(min=3, max=3)
        ]
    )
    bid_rate = IntegerField('Bid',
    validators=[
        DataRequired(),
        Length(min=1, max=10)
        ]
    )
    ask_rate = IntegerField('Ask',
    validators=[
        DataRequired(),
        Length(min=1, max=10)
        ]
    )

    submit = SubmitField('Add')


class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')