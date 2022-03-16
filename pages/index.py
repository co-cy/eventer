from flask import Blueprint, render_template, abort
from database.event import Event
from datetime import datetime
from flask_loguru import logger

blueprint = Blueprint("index", __name__)


@blueprint.route("/", methods=["GET"])
@logger.catch(onerror=lambda _: abort(500))
def index():
    logger.info("Someone went to the main page")
    events = Event.query.filter(Event.end_date >= datetime.utcnow()).all()
    return render_template("index.html", events=events)
