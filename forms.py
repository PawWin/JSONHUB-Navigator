from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField


class SearchNumberForm(FlaskForm):
    bottom = IntegerField()
    top = IntegerField()
    search = SubmitField()


class SearchWordForm(FlaskForm):
    word = StringField()
    search = SubmitField()

class DisplayCountForm(FlaskForm):
    myChoices = ['5', '10', '20', '50', '100']
    myField = SelectField(u'Field name', choices=myChoices)