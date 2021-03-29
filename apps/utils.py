from urllib.parse import urlparse
import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup


def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def scrapper(source):
    article_list = []
    try:
        r = requests.get(source.get("link"))
        soup = BeautifulSoup(r.content, features="xml")

        articles = soup.findAll("item")
        for a in articles:
            title = a.find("title").text
            link = a.find("link").text
            description = (
                a.find("description").text if a.find("description") else None
            )
            pubDate = a.find("pubDate").text
            article = {
                "source": source.get("name"),
                "title": title,
                "link": link,
                "pubDate": parse(pubDate),
                "description": description,
            }
            article_list.append(article)
        return article_list
    except Exception as e:
        return e
