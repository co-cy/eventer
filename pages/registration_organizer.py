from flask import Blueprint, redirect, url_for, abort, render_template
from forms.registration_organizer import RegistrationOrganizerForm
from database import db, organizer
from flask_loguru import logger
from datetime import datetime
from config import SaveConfig
from os.path import join

blueprint = Blueprint("registration_organizer", __name__)


@blueprint.route('/registration_organizer', methods=['GET'])
@blueprint.route('/registration_org', methods=['GET'])
@blueprint.route('/reg_org', methods=['GET'])
@blueprint.route('/reg_o', methods=['GET'])
@logger.catch(onerror=lambda _: abort(500))
def get_registration_organizer():
    logger.info("Someone went to the organizer registration page")
    form = RegistrationOrganizerForm()
    return render_template("registration_organizer.html", form=form)


@blueprint.route("/registration_organizer", methods=["POST"])
@blueprint.route("/registration_org", methods=["POST"])
@blueprint.route("/reg_org", methods=["POST"])
@blueprint.route("/reg_o", methods=["POST"])
@logger.catch(onerror=lambda _: abort(500))
def post_registration():
    logger.info("Someone sent an application for registration organizer")
    form = RegistrationOrganizerForm()
    if form.validate_on_submit():
        # TODO костыльный метод сохранения изображения мероприятия
        image = form.image.data

        filename = f"{round(datetime.utcnow().timestamp() * 1e7)}.{image.filename.split('.')[-1]}"
        img_path = join(SaveConfig.IMAGE_SAVE_DIR, filename)
        image.save(img_path)
        logger.info("Saved user image to {}", img_path)

        new_user = organizer.Organizer(img_path, form.name.data, form.description.data,
                                       form.phone.data, form.email.data, form.password.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index.index'))

    logger.info("The attempt to registration organizer failed. Errors occurred: {}", form.errors)
    return render_template("registration.html", form=form)

