from flask import Blueprint, render_template, redirect, url_for
from forms.registration_user import RegistrationUserForm
from flask_loguru import logger
from config import SaveConfig
from datetime import datetime
from database import db, user
from os.path import join

blueprint = Blueprint("registration", __name__)


@blueprint.route("/registration", methods=["GET"])
@blueprint.route("/reg", methods=["GET"])
def get_registration():
    logger.info("Someone went to the user registration page")
    form = RegistrationUserForm()
    return render_template("registration.html", form=form)


@blueprint.route("/registration", methods=["POST"])
@blueprint.route("/reg", methods=["POST"])
def post_registration():
    logger.info("Someone sent an application for registration")
    form = RegistrationUserForm()
    if form.validate_on_submit():
        # TODO костыльный метод сохранения изображения мероприятия
        image = form.image.data

        filename = f"{round(datetime.utcnow().timestamp() * 1e7)}.{image.filename.split('.')[-1]}"
        img_path = join(SaveConfig.IMAGE_SAVE_DIR, filename)
        image.save(img_path)
        logger.info("Saved user image to {}", img_path)

        new_user = user.User(img_path, form.first_name.data, form.last_name.data,
                             form.nickname.data, form.description.data, form.email.data,
                             form.password.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index.index'))

    logger.info("The attempt to registration failed. Errors occurred: {}", form.errors)
    return render_template("registration.html", form=form)
