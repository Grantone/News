from flask import render_template
from app import app
from .request import get_sources
from .request import get articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Wananchi News Review Web'
    return render_template('index.html', title = title)


@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)
