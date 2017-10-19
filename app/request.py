from app import app
import urllib.request,json
from .models import article
from .models import source

Article = article.Article
Source = source.Source


# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
