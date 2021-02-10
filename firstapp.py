import feedparser

from flask import Flask

app = Flask(__name__)

wsb = 'https://reddit.com/r/wallstreetbets/.rss'

@app.route("/")
def Get_feed():
        d=feedparser.parse(wsb)
        first_article = d['entries'][0]
        return  """<html>
		<body><h1> WallStreet Bets Reddit Barton</h1>
			<b>{0}</b></br>
			<i>{1}</i></br>
			<p>{2}</p>
		</body>
	</html>""".format(first_article.get('title'), first_article.get('summary'),first_article.get('subtitle'))

if __name__ == '__main__':
        app.run(host='0,0,0,0' debug=True)

