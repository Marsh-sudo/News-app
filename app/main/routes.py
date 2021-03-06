
from flask import render_template
from . import main
from app import app
from ..request import get_sources,get_articles

#views
@main.route('/')
def index():
    '''
    view root page that returns index page
    '''
    universal_news = get_sources('universal')
    sport_news = get_sources('sports')
    business_news = get_sources('business')
    news_sources = get_sources('general')
    print(news_sources)
    title = 'Home - Welcome to The best Online News Website'
    return render_template('base.html', title = title, news_sources=news_sources,universal_news=universal_news,sport_news=sport_news,business_news=business_news)

@app.route('/Articles/<int:news_id>')
def sourceArticle(id):
     '''
    view news page function that returns the news details page and its data
     '''
     general_articles = get_articles(id)
     print(general_articles)
     return render_template('sources.html',articles = general_articles)

@main.route('/Global-Articles')
def NewsArticle():
    '''
    routes that returns the news article
    '''
    tech_article = get_articles('tech')
  
    return render_template('article.html' ,tech = tech_article )