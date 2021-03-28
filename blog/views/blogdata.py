from flask import request, jsonify
from flask.views import MethodView

from apps.utils import is_url
from apps.exceptions import (
    serialize_exceptions,
    InvalidRequestException,
    EntityDoesNotExistException,
)

from blog.models import BlogSource
from blog.gateways import BlogDataGateway


class BlogDataAPI(MethodView):
    def __init__(self):
        super()
        self.gateway = BlogDataGateway()

    @serialize_exceptions
    def get(self):
        pass

    @serialize_exceptions
    def post(self):
        pass

    @serialize_exceptions
    def delete(self, id):
        pass

    @serialize_exceptions
    def put(self, id):
        pass
