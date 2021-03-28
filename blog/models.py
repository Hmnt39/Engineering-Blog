"""Data models."""
from apps.mixins import BaseMixin
from apps import db


class BlogSource(BaseMixin):
    """Data model for Blog Sources"""

    __tablename__ = "blog_source"

    name = db.Column(db.String(32), index=True, unique=False, nullable=False)
    feed_link = db.Column(
        db.String(512), index=False, unique=False, nullable=False
    )

    def __repr__(self):
        return f"Source - {self.name}"


class BlogData(BaseMixin):
    """Data model for Blog Data"""

    __tablename__ = "blog_data"

    source_id = db.Column(db.Integer, db.ForeignKey("blog_source.id"))
    source = db.relationship("BlogSource", backref="blog_source")
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
        return f"Blog {self.source} - {self.id}"
