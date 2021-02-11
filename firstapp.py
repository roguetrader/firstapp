import feedparser

from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc':'https://feeds.bbci.co.uk/news/rss.xml',
		'cnn':'http://rss.cnn.com/rss/edition.rss',
		'iol':'https://rss.iol.io/iol/news',
		'fox':'http://feeds.foxnews.com/foxnews/latest',
		'reddit':'https://reddit.com/r/worldnews/.rss',
		'de':'feeds.feedburner.com/daily-express-world-news',
		'spain':'https://feeds.thelocal.com/rss/es',
		'world':'https://world.wng.org/taxonomy/term/72/feed',
		'patriot':'https://patriotrising.com/feed'}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
        feed=feedparser.parse(RSS_FEEDS[publication])
        first_article = feed['entries'][0]
       	return  render_template("home.html", 
					title=first_article.get("title"),
					published=first_article.get("published"),
					summary=first_article.get("summary"))

if __name__ == '__main__':
        app.run()

