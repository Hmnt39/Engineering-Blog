from flask import current_app as app
from blog.views import SourceAPI, BlogDataAPI, ScrapperAPI


source_view = SourceAPI.as_view("source_api")
blog_view = BlogDataAPI.as_view("blog_api")
scrapper_view = ScrapperAPI.as_view("scrapper_api")

app.add_url_rule("/source/", view_func=source_view, methods=["POST", "GET"])
app.add_url_rule(
    "/source/<int:source_id>/",
    view_func=source_view,
    methods=["PUT", "DELETE"],
)
app.add_url_rule("/blog/", view_func=blog_view, methods=["POST", "GET"])
app.add_url_rule(
    "/blog/<int:id>/",
    view_func=blog_view,
    methods=["PUT", "DELETE"],
)
app.add_url_rule("/scrap/", view_func=scrapper_view, methods=["GET"])
