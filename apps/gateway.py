from flask import request, url_for
from apps import db
from urllib import parse


class BaseGateway:
    __abstract__ = True

    def __init__(self):
        pass

    def _decode_object(self, entity):
        return entity

    def _paginate_queryset(self, data, page=1, page_size=10, paginate=False):
        if paginate:
            data = data.paginate(
                page=page, per_page=page_size, error_out=False
            )
            url = request.base_url
            next_url = None
            prev_url = None
            if data.has_next:
                args = parse.urlencode(
                    {"page": data.next_num, "page_size": page_size}
                )
                next_url = url + "?" + args
            if data.has_prev:
                args = parse.urlencode(
                    {"page": data.prev_num, "page_size": page_size}
                )
                next_url = url + "?" + args
            count = data.total if data.total else 0
            return {
                "results": [
                    self._decode_object(entity) for entity in data.items
                ],
                "count": count,
                "previous": prev_url,
                "next": next_url,
            }
        else:
            return {
                "results": [self._decode_object(entity) for entity in data]
            }
