from flask import Blueprint, render_template, abort
from flask_loguru import logger
from database import organizer

blueprint = Blueprint("organizer", __name__)


@blueprint.route('/organizer/<int:id_org>', methods=['GET'])
@blueprint.route('/org/<int:id_org>', methods=['GET'])
@logger.catch(onerror=lambda _: abort(500))
def get_organizer(id_org: int):
    org = organizer.Organizer.query.get(id_org)
    if org:
        return render_template('organizer.html', organizer=org)
    return abort(404)
