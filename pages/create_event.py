from flask import current_app, redirect, url_for
from flask import Blueprint, render_template
from forms.event import CreateEventForm
from database import event, db
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
        image_path = join(current_app.config["IMAGE_SAVE_DIR"], image.filename)
        image.save(image_path)

        new_event = event.Event(image_path, form.annotation.data, form.description.data)

        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for("index.index"))
    return render_template("create_event.html", form=form)
