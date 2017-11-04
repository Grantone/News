class Articles:
    '''
    article class to define article Objects
    '''

    def __init__(self, author, title, description, urlToImage, image, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.image = image
        self.publishedAt = publishedAt


class Sources:
    '''
    Source class to define Source Objects
    '''

    def __init__(self, id, name, description, source, category):
        self.id = id
        self.name = name
        self.description = description
        self.source = source
        self.category = category
