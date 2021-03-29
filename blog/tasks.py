from blog.gateways import SourceGateway
from apps.utils import scrapper
import random


def build_blog_list():
    blogs = []
    sources = SourceGateway().get_sources()["results"]
    for source in sources:
        try:
            articles = scrapper(source)
            blogs.extend(articles)
        except Exception as e:
            pass
    random.shuffle(blogs)
    return blogs
