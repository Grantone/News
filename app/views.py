from flask import render_template,request,redirect,url_for
from app import app
from .request import get_source,get_source
from .request import get_articles,get_article,search_article

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

    # Getting popular article
    popular_sources = get_sources('popular')
    watched_article = get_articles('watched')
    sports_article = get_articles('sports')
    # print(popular_sources)
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


@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',article = searched_articles)
