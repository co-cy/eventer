class Config(dict):
    """Basic configuration class"""

    def __getallconfigs__(self) -> dict:
        """Returns all user-defined configurations"""
        return {x: self.__class__.__dict__[x] for x in self.__class__.__dict__.keys() if not x.startswith("__")}

    def __init__(self, *args, **kwargs):
        """Initializes the dictionary"""
        if len(args) == 1 and isinstance(args[0], dict):
            kwargs |= args[0]
        else:
            for key, item in enumerate(args):
                if not kwargs.get(key, None):
                    kwargs[key] = item
        list_arg = self.__getallconfigs__() | kwargs
        super().__init__(list_arg)


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


# For loguru
# More config
# https://loguru.readthedocs.io/en/stable/overview.html
class LoguruConfig(Config):
    sink = "log/file.log"
    rotation = "23:59"
    retention = "32 days"
    compression = "zip"
    catch = True

