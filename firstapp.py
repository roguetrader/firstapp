import feedparser

from flask import Flask

app = Flask(__name__)

#wsb = 'https://reddit.com/r/wallstreetbets/.rss'
wsb = 'https://feeds.bbci.co.uk/news/rss.xml'

@app.route("/")
def Get_feed():
        d=feedparser.parse(wsb)
	for i range(10):
	        first_article = d['entries'][i]
        		return  """<html>
			<body><h1> Feed Parsing</h1>
				<b>{0}</b></br>
				<i>{1}</i></br>
				<p>{2}</p>
			</body>
		</html>""".format(first_article.get('title'), first_article.get('published'),first_article.get('summary'))

if __name__ == '__main__':
        app.run()

