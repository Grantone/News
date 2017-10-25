import urllib.request,json
from .models import Articles, Sources

# Getting api key
api_key = None
# Getting the source base url
source_base_url = None
article_base_url = None

def configure_request(app):
    global api_key,source_base_url
    api_key = app.config['NEWS_API_KEY']

    # Article and Sourse base APIs
    source_base_url = app.config['NEWS_SOURCES_API_BASE_URL']
    article_base_url = app.config'[NEWS_ARTICLES_API_BASE_URL']

def get_source():
    '''
    Function that gets the json response to our url request
    '''

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
        name = source_item.get('original_name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        # if name:
        #     source_object = Source(id,name,description,url,category)
        #     source_results.append(source_object)

    return source_results

def get_article(source):

        get_article_url = article_url.format(source,api_key)
        print(get_article_url)

    '''
    Function that gets the json response to our urlrequest
    '''

    with urllib.request.urlopen(get_article_url) as url:
        get_article_url_data = url.read()
        get_articles_response =json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']
            id = article_details_response.get('id')
            title =                             article_results_response.get('article_result')
            # overview = article_details_response.get('overview')
            # poster = article_details_response.get('poster_path')
            # vote_average = article_details_response.get('poster_path')
            # vote_count = article_details_response.get('vote_count')

            # article_object = Article(id,title,overview,poster,vote_average,vote_count)



    return article_object

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
        time = article_item.get('time')

        if title:
            article_object = Article(author,title,description,urlToImage,publishedAt,time)
            article_results.append(article_object)

    print(article_object)
    return article_results



def search_article(article_name):
    search_article_url = 'https://api.thearticledb.org/3/search/article?api_key={}&query={}'.format(api_key,article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            search_article_list = search_article_response['results']
            search_article_results = process_results(search_article_list)


    return search_article_results
