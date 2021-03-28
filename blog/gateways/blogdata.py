from flask import jsonify, url_for
from apps.exceptions import EntityDoesNotExistException
from apps import db
from apps.gateway import BaseGateway
from blog.models import BlogData


class BlogDataGateway(BaseGateway):
    def __init__(self):
        self.model = BlogData

    def _decode_object(self, entity):
        return {
            "id": entity.id,
            "source": entity.source.name,
            "title": entity.title,
            "link": entity.feed_link,
            "pubDate": entity.pubDate,
            "description": entity.description,
        }
