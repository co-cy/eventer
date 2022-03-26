from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, file


class RegistrationOrganizerForm(FlaskForm):
    # TODO Добавить обработку ошибок
    image = file.FileField("Выберите свою картинку", validators=[file.FileRequired(), file.FileAllowed(["jpg", "png"])])

    name = StringField("Введите имя компании:", validators=[DataRequired()])

    description = StringField("Укажите полное описание", validators=[DataRequired()])

    phone = StringField("Введите контактный телефон", validators=[DataRequired()])
    email = EmailField("Введите вашу почту", validators=[DataRequired()])

    password = PasswordField("Укажите пароль", validators=[DataRequired()])
    submit = SubmitField("Создать")
