class Article:
    '''
    article class to define article Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://newsapi.org/v1/articles" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count



class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://newsapi.org/v1/sources" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
