from flask import render_template, request, redirect, url_for
from ..request import get_articles, get_article, search_article,get_sources, get_source, search_source
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular
    sources = get_sources()


    title = 'Home - Welcome to Wananchi News Review Web'
    return render_template('index.html', title = title, sources = sources)



@main.route('/articles')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular article
    popular_sources = get_sources('popular')
    watched_article = get_articles('watched')
    sports_article = get_articles('sports')
    # print(popular_sources)
    title = 'Home - Welcome to Wananchi News Review Web'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
else:
    return render_template('index.html', title = title,popular = popular_articles, watched =watched_article, sports = sports_article)




@main.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''

    article = get_article(id)
    title = f'{article.title}'
    reviews = Review.get reviews(article.id)

    return render_template('article.html',title = title,article = article,reviews = reviews)


@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',article = searched_articles)
