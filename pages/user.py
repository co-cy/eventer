from flask import Blueprint, render_template, abort
from flask_loguru import logger
from database import user


blueprint = Blueprint("user", __name__)


@blueprint.route('/user/<int:id_user>', methods=['GET'])
@logger.catch(onerror=lambda _: abort(500))
def get_user(id_user: int):
    u = user.User.query.get(id_user)
    logger.info("Someone tried to get a user with an id - {} ({})", id_user, u is None)
    if u:
        return render_template("user.html", user=u)
    return abort(404)
