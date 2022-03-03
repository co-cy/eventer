from pages import init_pages
from flask import Flask
from database import db

app = Flask(__name__)
app.config.from_pyfile('server_config.py')

db.init_app(app)
with app.app_context():
    db.create_all()

init_pages(app)
