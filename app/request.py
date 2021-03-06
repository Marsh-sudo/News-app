
import urllib.request,json

from app.tests.news_test import Sources

# from app.news_test import Articles
from .models import Sources,Articles
from config import Config
from app import app





def configure_request(app):
    global api_key,base_url,base_url_2
from instance.config import NEWS_API_KEY

api_key=app.config['NEWS_API_KEY']
#getting the base url
base_url = app.config['SOURCE_API_BASE_URL']
base_url_2 = app.config['ARTICLES_API_BASE_URL']

# Getting api key
# api_key = None
# Getting the movie base url
# base_url = None


def get_sources(category):
    '''
    function that gets json response to our url requests
    '''
    mark = app.config['NEWS_KEY']
    sources = app.config['SOURCES_API_BASE_URL']
    get_sources_url = sources.format(category,mark)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['general']:
            sources_results_list = get_sources_response['general']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    '''
    function that processes the sources result and transform them to a list of objects

    Args:
       sources_list:A list of dictionaries that contain sources list

       Returns:
          sources_results:A list of sources objects
    '''

    sources_results =[]
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Sources(id,name,description,url,language,country)
        sources_results.append(sources_object)


    return sources_results


def get_articles(source):
#     '''
#     function that gets the json response to our Url request
#     '''
    mark = app.config['NEWS_KEY']
    articles = app.config['ARTICLES_API_BASE_URL']
    get_articles_url = articles.format(source,mark)

    get_articles_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_articles_url)as url:
         get_articles_data = url.read()
         get_articles_response = json.loads(get_articles_data)

         articles_results = None

         if get_articles_response['results']:
             articles_results_list = get_articles_response['results']
             articles_results = process_results(articles_results_list)

             return articles_results



def process_results(articles_list):
    '''
    function that process the articles results and transform them to a list of objects 
    '''

    articles_results = []
    for article_item in articles_list:
        id = article_item('id')
        title = article_item('title')
        author = article_item('author')
        description = article_item('description')
        urlToImage = article_item('urlToImage')
        url = article_item('url')

        articles_object = Articles(id,author,title,description,url,urlToImage)
        articles_results.append(articles_object)
     
    return articles_results


