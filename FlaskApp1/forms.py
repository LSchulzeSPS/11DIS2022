from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from FlaskApp1.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

class CalculatorForm(FlaskForm):
    num1 = FloatField("Num1", validators=[DataRequired()])
    num2 = FloatField("Num2", validators=[DataRequired()])

class CalcDFForm(FlaskForm):
    num1 = IntegerField("Num1", validators=[DataRequired(), Length(min=1, max=10)])
    num2 = IntegerField("Num2", validators=[DataRequired(), Length(min=1, max=10)])
    submit = SubmitField("Register Now")

class letterCountForm(FlaskForm):
    word = StringField("Word", validators=[DataRequired()])
    submit = SubmitField("Submit Word")
