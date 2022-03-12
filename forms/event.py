from wtforms import StringField, SubmitField, DateTimeLocalField
from wtforms.validators import DataRequired
from datetime import datetime, timedelta
from flask_wtf import FlaskForm, file


class CreateEventForm(FlaskForm):
    # TODO: Прописать валидаторы полей
    image = file.FileField(validators=[file.FileRequired(), file.FileAllowed(["jpg", "png"])])
    annotation = StringField("Укажите аннотация", validators=[DataRequired()])
    description = StringField("Укажите полное описание", validators=[DataRequired()])
    # Учесть длину адреса
    location = StringField("Укажите местоположение мероприятия", validators=[DataRequired()])

    reg_start_date = DateTimeLocalField("Укажите начало регистрации на мероприятия",
                                        default=datetime.utcnow() + timedelta(minutes=5),
                                        format='%Y-%m-%dT%H:%M',
                                        validators=[DataRequired()])
    reg_end_date = DateTimeLocalField("Укажите дату закрытия регистрации на мероприятия",
                                      default=datetime.utcnow() + timedelta(days=1),
                                      format='%Y-%m-%dT%H:%M',
                                      validators=[DataRequired()])
    start_date = DateTimeLocalField("Укажите начало мероприятия",
                                    default=datetime.utcnow() + timedelta(minutes=5),
                                    format='%Y-%m-%dT%H:%M',
                                    validators=[DataRequired()])
    end_date = DateTimeLocalField("Укажите дату завершения мероприятия",
                                  default=datetime.utcnow() + timedelta(days=1),
                                  format='%Y-%m-%dT%H:%M',
                                  validators=[DataRequired()])
    submit = SubmitField("Создать")
