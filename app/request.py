from app import app
import urllib.request,json
from .models import article
from .models import source

Article = article.Article
Source = source.Source


# Getting api key
# api_key = app.config['NEWS_API_KEY']


# Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]


def get_source():
    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_url_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_results_response['sources']
            source_results = process_sources(source_results_list)


    return source_results
