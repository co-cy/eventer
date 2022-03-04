from database import db


class Event(db.Model):
    id = db.Column(db.INTEGER, index=True, primary_key=True)

    image_path = db.Column(db.Text, nullable=False, unique=True)
    annotation = db.Column(db.Text, nullable=False)

    description = db.Column(db.Text, nullable=False)

    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, image: str, annotation: str, description: str) -> None:
        self.image_path = image
        self.annotation = annotation
        self.description = description
