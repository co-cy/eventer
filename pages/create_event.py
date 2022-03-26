from flask import Blueprint, render_template, abort
from forms.event import CreateEventForm
from flask import redirect, url_for
from database import event, db
from flask_loguru import logger
from config import SaveConfig
from datetime import datetime
from os.path import join

blueprint = Blueprint("create_event", __name__)


@blueprint.route("/create_event", methods=["GET"])
@blueprint.route("/create", methods=["GET"])
@logger.catch(onerror=lambda _: abort(500))
def create_event_get():
    logger.info("Someone went to the creation page event")
    form = CreateEventForm()
    return render_template("create_event.html", form=form)


@blueprint.route("/create_event", methods=["POST"])
@blueprint.route("/create", methods=["POST"])
@logger.catch(onerror=lambda _: abort(500))
def create_event_post():
    logger.info("Someone tried to create an event")
    form = CreateEventForm()
    if form.validate_on_submit():
        # TODO костыльный метод сохранения изображения мероприятия
        image = form.image.data

        filename = f"{round(datetime.utcnow().timestamp() * 1e7)}.{image.filename.split('.')[-1]}"
        img_path = join(SaveConfig.IMAGE_SAVE_DIR, filename)
        image.save(img_path)
        logger.info("Saved event picture: {}", img_path)

        new_event = event.Event(img_path, form.annotation.data, form.description.data,
                                form.location.data,
                                form.reg_start_date.data, form.reg_end_date.data,
                                form.start_date.data, form.end_date.data)

        db.session.add(new_event)
        db.session.commit()

        logger.info("Event created. Event ID - {}", new_event.id)

        return redirect(url_for("index.index"))
    logger.info("The attempt to create events failed. Errors occurred: {}", form.errors)
    return render_template("create_event.html", form=form)
