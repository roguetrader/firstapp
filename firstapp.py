import feedparser

from flask import Flask

app = Flask(__name__)

#wsb = 'https://reddit.com/r/wallstreetbets/.rss'
RSS_FEEDS = {'bbc':'https://feeds.bbci.co.uk/news/rss.xml',
		'cnn':'http://rss.cnn.com/rss/edition.rss',
		'iol':'https://rss.iol.io/iol/news'
		'fox':'http://feeds.foxnews.com/foxnews/latest'}

@app.route("/")
@app.route("/bbc")
def bbc():
	return get_news('bbc')

@app.route("/fox")
def cnn():
	return get_news('fox')

@app.route("iol")
def iol():
	return get_news('iol')

def get_news(publication):
        feed=feedparser.parse(RSS_FEEDS[publication])
        first_article = feed['entries'][0]
       	return  """<html>
		<body><h1> Feed Parsing</h1>
			<b>{0}</b></br>
			<i>{1}</i></br>
			<p>{2}</p>
		</body>
	</html>""".format(first_article.get('title'), first_article.get('published'),first_article.get('summary'))

if __name__ == '__main__':
        app.run()

