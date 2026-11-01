from server.app import app
from models import Event, db

with app.app_context():
    events = Event.query

__all__ = ["app", "events", "Event", "db"]
