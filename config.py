class Config(dict):
    def __init__(self):
        list_arg = {x: self.__class__.__dict__[x] for x in self.__class__.__dict__.keys() if not x.startswith("__")}
        super().__init__(**list_arg)


# For main app
# More config
# https://flask.palletsprojects.com/en/2.0.x/config/
class FlaskConfig(Config):
    DEBUG = True
    SECRET_KEY = "12345"


# For database
# More config
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
class SqlalchemyConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///./database/database.db"


# For image saving system
class SaveConfig(Config):
    IMAGE_SAVE_DIR = "static/user_images"


# For Celery
# More config
# https://docs.celeryproject.org/en/stable/userguide/configuration.html
class CeleryConfig(Config):
    result_backend = "db+sqlite:///./database/database.db"
    broker_url = 'pyamqp://guest:guest@79.120.76.23:5672/'

