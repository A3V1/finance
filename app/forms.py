from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class FinancialDataForm(FlaskForm):
    income = FloatField('Income', validators=[DataRequired()])
    expenses = FloatField('Expenses', validators=[DataRequired()])
    savings = FloatField('Savings', validators=[DataRequired()])
    investments = FloatField('Investments', validators=[DataRequired()])
    goals = StringField('Financial Goals')
    submit = SubmitField('Submit')
