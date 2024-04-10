from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField


class SearchNumberForm(FlaskForm):
    bottom = IntegerField(render_kw={'class': 'bg-dark text-white'})
    top = IntegerField(render_kw={'class': 'bg-dark text-white'})
    search = SubmitField("Search", render_kw={'class': 'btn btn-primary'})


class SearchWordForm(FlaskForm):
    word = StringField()
    search = SubmitField("Search", render_kw={'class': 'btn btn-primary'})
