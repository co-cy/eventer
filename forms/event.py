from flask_wtf import FlaskForm, file
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateEventForm(FlaskForm):
    image = file.FileField(validators=[file.FileRequired(), file.FileAllowed(["jpg", "png"])])
    annotation = StringField("Укажите анатацию", validators=[DataRequired()])
    description = StringField("Укажите полное описание", validators=[DataRequired()])
    submit = SubmitField("Создать")
