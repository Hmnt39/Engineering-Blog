from flask import jsonify, url_for
from apps.exceptions import EntityDoesNotExistException
from apps import db
from apps.gateway import BaseGateway
from blog.models import BlogSource


class SourceGateway(BaseGateway):
    def __init__(self):
        self.model = BlogSource

    def _decode_object(self, entity):
        return {
            "id": entity.id,
            "name": entity.name,
            "link": entity.feed_link,
        }

    def get_sources(self, ids=[], page=1, page_size=10, paginate=False):
        sources = self.model.query
        if ids:
            sources = sources.filter(self.model.id.in_(ids))
        return self._paginate_queryset(
            data=sources, page=page, page_size=page_size, paginate=paginate
        )

    def add_source(self, name, link):
        source = self.model(name=name, feed_link=link)
        db.session.add(source)
        db.session.commit()
        return self._decode_object(source)

    def delete_source(self, source_id):
        source = self.model.query.filter(self.model.id == source_id).first()
        if source:
            db.session.delete(source)
            db.session.commit()
        else:
            raise EntityDoesNotExistException()
        return jsonify({"id": source.id})

    def update_source(self, id, name=None, link=None):
        source = self.model.query.filter(self.model.id == id).first()
        if not source:
            raise EntityDoesNotExistException()
        source.name = name if name else source.name
        source.feed_link = link if link else source.feed_link
        db.session.commit()
        return self._decode_object(source)
