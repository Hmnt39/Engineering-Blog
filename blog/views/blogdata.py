from flask import request, jsonify
from flask.views import MethodView
from dateutil.parser import parse

from apps.utils import is_url
from apps.exceptions import (
    serialize_exceptions,
    InvalidRequestException,
    EntityDoesNotExistException,
)

from blog.models import BlogSource
from blog.gateways import BlogDataGateway, SourceGateway


class BlogDataAPI(MethodView):
    def __init__(self):
        super()
        self.gateway = BlogDataGateway()

    @serialize_exceptions
    def get(self):
        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 10))
        paginate = request.args.get("paginate", True)
        ids = request.args.get("ids", [])
        source = request.args.get("source", None)
        try:
            ids = json.loads(ids)
        except:
            ids = []
        return jsonify(
            self.gateway.get_blogs(
                ids=ids,
                source=source,
                page=page,
                page_size=page_size,
                paginate=paginate,
            )
        )

    @serialize_exceptions
    def post(self):
        request_data = request.get_json()
        title = request_data.get("title", "")
        link = request_data.get("link", "")
        source = request_data.get("source", "")
        description = request_data.get("description", "")
        pubDate = request_data.get("pubDate", None)
        if source:
            source_exists = SourceGateway().filter_source(name=source)
            if not source_exists:
                raise InvalidRequestException(message="Invalid Source")
        try:
            pubDate = parse(str(pubDate))
        except:
            pubDate = None
        if not is_url(link):
            raise InvalidRequestException(message="Invalid URL Link")
        exist_blog = self.gateway.filter_blog(
            source=source_exists, date=pubDate
        )
        if exist_blog:
            raise InvalidRequestException(message="Blog already Exists")
        return self.gateway.add_blog(
            source=source_exists,
            title=title,
            link=link,
            pubDate=pubDate,
            description=description,
        )

    @serialize_exceptions
    def delete(self, id):
        return self.gateway.delete_blog(id=id)

    @serialize_exceptions
    def put(self, id):
        request_data = request.get_json()
        title = request_data.get("title", "")
        link = request_data.get("link", "")
        description = request_data.get("description", "")
        pubDate = request_data.get("pubDate", None)
        try:
            pubDate = parse(str(pubDate))
        except:
            pubDate = None
        if link and not is_url(link):
            raise InvalidRequestException(message="Invalid URL Link")
        return self.gateway.update_blog(
            id=id,
            title=title,
            link=link,
            description=description,
            pubDate=pubDate,
        )
