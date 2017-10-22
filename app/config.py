class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://api.thnewsdb.org/3/news/{}?api_key={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_KEY = 'eeca31cc2f7e487ba2a316385457b93d'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
