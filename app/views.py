from flask import render_template, request, redirect, url_for
from ..request import get_articles, get_article, search_article
from ..models import Review
from .forms import ReviewForm
from . import main

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

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
else:
    return render_template('index.html', title = title,popular = popular_articles, watched =watched_article, sports = sports_article)




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




@app.route('/article/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    article = get_article(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(article.id,title,article.poster,review)
        new_review.save_review()
        return redirect(url_for('article',id = article.id ))

    title = f'{article.title} review'
    return render_template('new_review.html',title = title, review_form=form, article=article)
