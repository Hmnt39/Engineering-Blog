"""Data models."""
from .mixins import TimestampMixin
from . import db


class BlogSource(TimestampMixin, db.Model):
    """Data model for Blog Sources"""

    __tablename__ = "blog_source"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=False, nullable=False)
    feed_link = db.Column(
        db.String(512), index=False, unique=False, nullable=False
    )

    def __repr__(self):
        return "<Source - {}}>".format(self.name)


class BlogData(TimestampMixin, db.Model):
    """Data model for Blog Data"""

    __tablename__ = "blog_data"

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(32), index=True, unique=False, nullable=False)
    title = db.Column(
        db.String(1024),
        index=False,
        unique=False,
        nullable=False,
    )
    link = db.Column(
        db.String(1024),
        index=False,
        unique=False,
        nullable=False,
    )
    pubDate = db.Column(
        db.DateTime,
        index=True,
        unique=False,
        nullable=False,
    )
    description = db.Column(
        db.String(1024),
        index=False,
        unique=False,
        nullable=True,
    )

    def __repr__(self):
        return "<Blog {} - {}>".format(self.source, self.id)
