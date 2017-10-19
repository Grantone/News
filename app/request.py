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



    # Getting the article base url
    base_url = app.config['ARTICLE_API_BASE_URL']

def get_article():
    '''
    Function that gets the json response to our urlrequest
    '''

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_url_data = url.read()
        get_articles_response =json.loads(get_articless_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list =get_results_response['articles']
            article_results =process_articles(article_results_list)


    return article_results





def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('original_name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        if name:
            source_object = Source(id,name,description,url,category)
            source_results.append(source_object)

    return source_results
