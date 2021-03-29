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
            "source_id": entity.source.id,
            "title": entity.title,
            "link": entity.link,
            "pubDate": str(entity.pubDate),
            "description": entity.description,
        }

    def get_blogs(
        self, ids=[], source=None, page=1, page_size=10, paginate=False
    ):
        blogs = self.model.query
        if source:
            blogs = blogs.filter(self.model.source.name == source)
        if ids:
            blogs = blogs.filter(self.model.id.in_(ids))
        return self._paginate_queryset(
            data=blogs, page=page, page_size=page_size, paginate=paginate
        )

    def filter_blog(self, source, date):
        blogs = self.model.query
        if source:
            blogs = blogs.filter(self.model.source == source)
        if date:
            blogs = blogs.filter(self.model.pubDate == date)
        return blogs.first()

    def add_blog(self, source, title, link, pubDate, description):
        blog = self.model(
            source=source,
            title=title,
            link=link,
            pubDate=pubDate,
            description=description,
        )
        db.session.add(blog)
        db.session.commit()
        return self._decode_object(blog)

    def delete_blog(self, id):
        blog = self.model.query.filter(self.model.id == id).first()
        if blog:
            db.session.delete(blog)
            db.session.commit()
        else:
            raise EntityDoesNotExistException()
        return jsonify({"id": blog.id})

    def update_blog(
        self, id, title=None, link=None, pubDate=None, description=None
    ):
        blog = self.model.query.filter(self.model.id == id).first()
        if not blog:
            raise EntityDoesNotExistException()
        blog.title = title if title else blog.title
        blog.link = link if link else blog.link
        blog.pubDate = pubDate if pubDate else blog.pubDate
        blog.description = description if description else blog.description
        db.session.commit()
        return self._decode_object(blog)
