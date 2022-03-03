from database import db


class Event(db.Model):
    id = db.Column(db.INTEGER, index=True, primary_key=True)

    image = db.Column(db.Text, nullable=False)
    annotations = db.Column(db.Text, nullable=False)

    description = db.Column(db.Text, nullable=False)

    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, image: str, annotations: str, description: str) -> None:
        self.image = image
        self.annotations = annotations
        self.description = description
