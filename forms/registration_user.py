from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, file


class RegistrationUserForm(FlaskForm):
    image = file.FileField("Выберите свою картинку", validators=[file.FileRequired(), file.FileAllowed(["jpg", "png"])])

    first_name = StringField("Введите ваше имя:", validators=[DataRequired()])
    last_name = StringField("Введите вашу фамилию:", validators=[DataRequired()])
    nickname = StringField("Введите ваш ник", validators=[DataRequired()])

    description = StringField("Укажите полное описание", validators=[DataRequired()])

    email = EmailField("Введите вашу почту", validators=[DataRequired()])

    password = PasswordField("Укажите пароль", validators=[DataRequired()])
    submit = SubmitField("Создать")
