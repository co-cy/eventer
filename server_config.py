DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///./database/database.db"
SECRET_KEY = "12345"
IMAGE_SAVE_DIR = "static/user_images"

# For Celery
CELERY_RESULT_BACKEND = "db+sqlite:///./database/database.db"
BROKER_URL = 'pyamqp://guest:guest@79.120.76.23:5672/'
