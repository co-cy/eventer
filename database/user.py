from database import db


user_event = db.Table(
    'user_event',
    db.Column('user_id', db.INTEGER, db.ForeignKey('user.id')),
    db.Column('event_id', db.INTEGER, db.ForeignKey("event.id"))
)


class User(db.Model):
    id = db.Column(db.INTEGER, index=True, primary_key=True)

    image = db.Column(db.Text)

    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    nickname = db.Column(db.String(32))

    description = db.Column(db.Text)

    email = db.Column(db.String(64))

    password = db.Column(db.String(128))

    events = db.relationship("Event", secondary=user_event, backref="users")
