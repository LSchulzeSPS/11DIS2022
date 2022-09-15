from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class romanNumeralsForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired()])

class isomorphicPairForm(FlaskForm):
    word1 = StringField("Word1", validators=[DataRequired()])
    word2 = StringField("Word2", validators=[DataRequired()])


