from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField


class SearchNumberForm(FlaskForm):
    bottom = IntegerField(render_kw={'class': 'bg-dark text-white'})
    top = IntegerField(render_kw={'class': 'bg-dark text-white'})
    search1 = SubmitField("Search", render_kw={'class': 'btn btn-primary mt-3 mb-1'})


class SearchWordForm(FlaskForm):
    word = StringField(render_kw={'class': 'bg-dark text-white'})
    search2 = SubmitField("Search", render_kw={'class': 'btn btn-primary mt-3'})
