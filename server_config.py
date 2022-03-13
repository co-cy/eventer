# For main app
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "12345"

# For database
SQLALCHEMY_DATABASE_URI = "sqlite:///./database/database.db"

# For image saving system
IMAGE_SAVE_DIR = "static/user_images"

# For Celery
CELERY_RESULT_BACKEND = "db+sqlite:///./database/database.db"
BROKER_URL = 'pyamqp://guest:guest@79.120.76.23:5672/'
