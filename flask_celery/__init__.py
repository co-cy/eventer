from celery import Celery
from flask import Flask


class MCelery(Celery):
    def init_app(self, app: Flask):
        self.conf.update(app.config)


celery = MCelery('celery')
