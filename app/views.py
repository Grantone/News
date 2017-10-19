from flask import render_template
from app import app
from .request import get_source
from .request import get_article

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


@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)
