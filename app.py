from pages import init_pages
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('server_config.py')

init_pages(app)

app.run()
