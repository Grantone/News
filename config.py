import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_API_BASE_URL ='https://newsapi.org/v1/sources?language=en&category={}'
    # NEWS_ARTICLES_API_BASE_URL ='https://newsapi.org/v1/articles?source={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
