import urllib.request
import json
from .models import Articles, Sources
# Source = sources.Sources
# Article = article.Articles

# Getting api key
api_key = None
# Getting the source base url
# source_base_url = None
# article_base_url = None


def configure_request(app):
    global api_key, source_base_url
    api_key = app.config['NEWS_API_KEY']

    # Article and Sourse base APIs
    # source_base_url = app.config['NEWS_SOURCES_API_BASE_URL']
    # article_base_url = app.config'[NEWS_ARTICLES_API_BASE_URL']


def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v1/sources'.format(
        category, api_key)

    with urllib.request.urlopen(source_base_url) as url:
        get_sources_url_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_results_response['sources']
            source_results = process_source_result(source_result_list)

    return source_results


def process_source_result(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
    source_list: A list of dictionaries thatcontain source details

    Returns :
    source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        source_object = Sources(id, name, description, url, category)
        source_results.append(source_object)

    return source_results


# def get_article(source):
#
#     get_article_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(
#         source, api_key)
#     # print(get_article_url)
#
#     '''
#         Function that gets the json response to our urlrequest
#         '''
#
#     with urllib.request.urlopen(get_article_url) as url:
#         get_article_data = url.read()
#         get_articles_response = json.loads(get_article_data)
#     #
#     article_results = None
#     #
#     if get_articles_response['articles']:
#         articles_results_list = get_articles_response['articles']
#         articles_results = process_results(articles_results_list)
#
#         return article_results


def get_article(source):
    get_article_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(
        source, api_key)
    print(get_article_url)
    '''
        Function that gets the json response to our urlrequest
        '''
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_articles_response = json.loads(get_article_data)
    #
    article_results = None
    #
    if get_articles_response['articles']:
        articles_results_list = get_articles_response['articles']
        articles_results = process_results(articles_results_list)
        return articles_results


# def process_results(articles_list):
#     '''
#     Function  that processes the article result and transform them to a list of Objects
#
#     Args:
#     source_list: A list of dictionaries that contain article details
#
#     Returns :
#     source_results: A list of article objects
#     '''
#     article_results = []
#
#     for article_item in articles_list:
#         author = article_item.get('author')
#         title = article_item.get('title')
#         description = article_item.get('description')
#         urlToImage = article_item.get('urlToImage')
#         publishedAt = article_item.get('publishedAt')
#         time = article_item.get('time')
#
#         article_object = Articles(
#             author, title, description, urlToImage, publishedAt, time)
#         article_results.append(article_object)
#         # source_results.append(source_object)
#
#     # print(article_object)
#     return article_results

def process_results(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
    source_list: A list of dictionaries that contain article details
    Returns :
    source_results: A list of article objects
    '''
    article_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        # time = article_item.get('time')
        article_object = Articles(
            author, title, description, urlToImage, publishedAt)
        article_results.append(article_object)
    return article_results


def search_article(article_name):
    search_article_url = 'https://api.thearticledb.org/3/search/article?api_key={}&query={}'.format(
        api_key, article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            search_article_list = search_article_response['results']
            search_article_results = process_results(search_article_list)

    return search_article_results


def get_sources():
    sources_url = 'https://newsapi.org/v1/sources?language=en'
    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources_results = None

        if sources_response['sources']:
            sources_list = sources_response['sources']
            print(len(sources_list))
            sources_results = process_source_result(sources_list)

    return sources_results
