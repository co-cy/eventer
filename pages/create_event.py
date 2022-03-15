from flask import Blueprint, render_template
from forms.event import CreateEventForm
from flask import redirect, url_for
from database import event, db
from config import SaveConfig
from datetime import datetime
from os.path import join

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

        filename = f"{round(datetime.utcnow().timestamp() * 1e7)}.{image.filename.split('.')[-1]}"
        img_path = join(SaveConfig.IMAGE_SAVE_DIR, filename)
        image.save(img_path)

        new_event = event.Event(img_path, form.annotation.data, form.description.data,
                                form.location.data,
                                form.reg_start_date.data, form.reg_end_date.data,
                                form.start_date.data, form.end_date.data)

        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for("index.index"))
    return render_template("create_event.html", form=form)
