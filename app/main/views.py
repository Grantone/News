from flask import render_template, request, redirect, url_for
from ..requests import get_article, get_source
from . import main


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    news == get_article()
    print(news)
    title = 'Home - Welcome to Wananchi News Review Web'
    return render_template('index.html', title = title, source = sources)



@main.route('/source/<id>')
def sources():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting sources request.args.get('sources_query')
    sources=get_article(id)
    source_id = id
    title = f'{source_id}'
    print(sources)
    return redirect(url_for('index.html',title = title,source=source,source_id=source_id ))



# @main.route('/article/<int:article_id>')
# def article(article_id):
#
#     '''
#     View article page function that returns the article details page and its data
#     '''
#
#     article = get_article(id)
#     title = f'{article.title}'
#     reviews = Review.get reviews(article.id)
#
#     return render_template('article.html',title = title,article = article,reviews = reviews)
#
#
# @main.route('/search/<article_name>')
# def search(article_name):
#     '''
#     View function to display the search results
#     '''
#     article_name_list = article_name.split(" ")
#     article_name_format = "+".join(article_name_list)
#     searched_articles = search_article(article_name_format)
#     title = f'search results for {article_name}'
#     return render_template('search.html',article = searched_articles)
