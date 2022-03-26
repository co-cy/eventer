from database import db


organizer_event = db.Table(
    'organizer_event',
    db.Column('organizer_id', db.INTEGER, db.ForeignKey('organizer.id')),
    db.Column('event_id', db.INTEGER, db.ForeignKey("event.id"))
)


class Organizer(db.Model):
    id = db.Column(db.INTEGER, index=True, primary_key=True)

    image = db.Column(db.Text)

    name = db.Column(db.String(64))

    description = db.Column(db.Text)

    phone = db.Column(db.INTEGER)
    email = db.Column(db.String(64))

    password = db.Column(db.String(128))

    events = db.relationship("Event", secondary=organizer_event, backref="organizers")
