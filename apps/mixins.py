from datetime import datetime
from . import db


class BaseMixin(db.Model):
    """ Mixins for TImestampable Models """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
