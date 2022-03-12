from celery import Celery
from flask import Flask


class MCelery(Celery):
    def init_app(self, app: Flask):
        self.conf.update(app.config)
        TaskBase = self.Task

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        self.Task = ContextTask


celery = MCelery('celery')
