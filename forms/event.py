from flask_wtf import FlaskForm, file
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime


class CreateEventForm(FlaskForm):
    # TODO: Прописать валидаторы полей
    image = file.FileField(validators=[file.FileRequired(), file.FileAllowed(["jpg", "png"])])
    annotation = StringField("Укажите анатацию", validators=[DataRequired()])
    description = StringField("Укажите полное описание", validators=[DataRequired()])
    start_date = DateTimeField("Укажите начало мероприятия", default=datetime.now(), validators=[DataRequired()])
    end_date = DateTimeField("Укажите дату закрытия мероприятия", validators=[DataRequired()])
    submit = SubmitField("Создать")
