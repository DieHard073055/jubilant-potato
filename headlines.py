from flask import Flask
from feedparser import parse
import json

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

''' 
    will return all the publications
'''
@app.route("/")
def get_pubs():
    pubs=[]
    for pub in RSS_FEEDS:
        pubs.append(pub)

    return json.dumps(pubs)

'''
    will return all article titles for 
    the given publication
'''
@app.route("/<pub>")
def get_news(pub):
    if pub in RSS_FEEDS:
        news_articles = []
        feed = parse(RSS_FEEDS[pub])
        for i in feed['entries']:
            news_articles.append(i.title)
        return json.dumps(news_articles)
    else:
        return json.dumps({"publications_that_dosent_exist":[pub]})

'''
    will return all the data for the news article
'''
@app.route("/<pub>/<num>")
def get_news_details(pub=None, num=0):
    if pub in RSS_FEEDS:
        num = int(num)
        feed = parse(RSS_FEEDS[pub])
        if len(feed['entries']) > num:
            return json.dumps(feed['entries'][num])
        else:
            return json.dumps({"wrong article num":num})
    else:
        return json.dumps({"wrong publication":pub})

if __name__ == '__main__':
    app.run(port=8080, debug=True)

