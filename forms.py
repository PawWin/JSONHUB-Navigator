from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField


class SearchNumberForm(FlaskForm):
    bottom = IntegerField(render_kw={'class': 'bg-dark text-white'})
    top = IntegerField(render_kw={'class': 'bg-dark text-white'})
    search1 = SubmitField("Search", render_kw={'class': 'btn btn-primary mt-3 mb-1'})


class SearchWordForm(FlaskForm):
    word = StringField(render_kw={'class': 'bg-dark text-white'})
    search2 = SubmitField("Search", render_kw={'class': 'btn btn-primary mt-3'})

class SelectForm(FlaskForm):
    # Define a select field with choices
    select_field = SelectField('Ilosc', choices=[('10', '10'), ('25', '25'), ('50', '50'), ('100', '100')],render_kw={'class': 'bg-dark text-white'})
    submit = SubmitField("Wyświetl", render_kw={'class': 'btn btn-primary mt-3'})