from flask import current_app, redirect, url_for
from flask import Blueprint, render_template
from forms.event import CreateEventForm
from database import event, db
from os.path import join
from time import time
from pytz import utc

from flask_celery.event.delete_event import delete_event

blueprint = Blueprint("create_event", __name__)


@blueprint.route("/create_event", methods=["GET"])
@blueprint.route("/create", methods=["GET"])
def create_event_get():
    form = CreateEventForm()
    return render_template("create_event.html", form=form)


@blueprint.route("/create_event", methods=["POST"])
@blueprint.route("/create", methods=["POST"])
def create_event_post():
    form = CreateEventForm()
    if form.validate_on_submit():
        image = form.image.data

        filename = f"{round(time() * 1e7)}.{image.filename.split('.')[-1]}"
        img_path = join(current_app.config["IMAGE_SAVE_DIR"], filename)
        image.save(img_path)

        new_event = event.Event(img_path, form.annotation.data, form.description.data,
                                form.start_date.data, form.end_date.data)

        db.session.add(new_event)
        db.session.commit()
        print("DATE END: ", form.end_date.data)
        delete_event.apply_async((new_event.id, ), eta=form.end_date.data)

        return redirect(url_for("index.index"))
    return render_template("create_event.html", form=form)
