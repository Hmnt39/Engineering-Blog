from flask import current_app as app
from blog.views import SourceAPI


source_view = SourceAPI.as_view("source_api")
app.add_url_rule("/source/", view_func=source_view, methods=["POST", "GET"])
app.add_url_rule(
    "/source/<int:source_id>/",
    view_func=source_view,
    methods=["PUT", "DELETE"],
)
