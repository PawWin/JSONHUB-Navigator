from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField


class SearchNumberForm(FlaskForm):
    bottom = IntegerField()
    top = IntegerField()
    search = SubmitField()


class SearchWordForm(FlaskForm):
    word = StringField()
    search = SubmitField()
