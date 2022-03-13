from celery import Celery
from flask import Flask


class MCelery(Celery):
    def init_app(self, app: Flask):
        self.conf.update(broker_url=app.config.get("BROKER_URL", None),
                         result_backend=app.config.get("CELERY_RESULT_BACKEND", None))
        TaskBase = self.Task

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        self.Task = ContextTask


celery = MCelery('celery')
