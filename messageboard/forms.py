from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

from messageboard import app

class MessageForm(FlaskForm):
    name = StringField('昵称', validators=[DataRequired(), Length(1,10)])
    body = TextAreaField('内容', validators=[DataRequired(), Length(1,500)])
    submit = SubmitField()

