from flask import render_template
from app import app
from .request import get_source,get_source
from .request import get_articles,get_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular articles
    popular_articles = get_articles('popular')
    print(popular_articles)


    title = 'Home - Welcome to Wananchi News Review Web'
    return render_template('index.html', title = title,popular = popular_articles)



@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_sources = get_sources('popular')
    print(popular_sources)
    title = 'Home - Welcome to Wananchi Source Review Web'
    return render_template('index.html', title = title,popular = popular_sources)




@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''

    article = get_article(id)
    title = f'{article}'

    return render_template('article.html',title = title,article = article)
