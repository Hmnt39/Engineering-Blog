from flask import request, jsonify
from flask.views import MethodView
import json

from apps.utils import is_url
from apps.exceptions import (
    serialize_exceptions,
    InvalidRequestException,
    EntityDoesNotExistException,
)

from blog.models import BlogSource
from blog.gateways import SourceGateway
from blog.tasks import build_blog_list


class SourceAPI(MethodView):
    def __init__(self):
        super()
        self.gateway = SourceGateway()

    @serialize_exceptions
    def get(self):
        page = int(request.args.get("page", 1))
        page_size = int(request.args.get("page_size", 10))
        paginate = request.args.get("paginate", True)
        ids = request.args.get("ids", [])
        name = request.args.get("name", None)
        try:
            ids = json.loads(ids)
        except:
            ids = []
        return jsonify(
            self.gateway.get_sources(
                ids=ids,
                name=name,
                page=page,
                page_size=page_size,
                paginate=paginate,
            )
        )

    @serialize_exceptions
    def post(self):
        request_data = request.get_json()
        name = request_data.get("name", "")
        link = request_data.get("link", "")
        if not is_url(link):
            raise InvalidRequestException(message="Invalid URL Link")
        return self.gateway.add_source(name=name, link=link)

    @serialize_exceptions
    def delete(self, source_id):
        return self.gateway.delete_source(source_id=source_id)

    @serialize_exceptions
    def put(self, source_id):
        request_data = request.get_json()
        name = request_data.get("name", None)
        link = request_data.get("link", None)
        if link and not is_url(link):
            raise InvalidRequestException(message="Invalid URL Link")
        return self.gateway.update_source(
            id=source_id,
            name=name,
            link=link,
        )


class ScrapperAPI(MethodView):
    @serialize_exceptions
    def get(self):

        ## TODO : Fetch blogs of the sources and add to DB.
        ## Add Threading to fetch mutiple source at an instant
        # articles = build_blog_list()
        return jsonify(True)
