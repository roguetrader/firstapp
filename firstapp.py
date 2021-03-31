import feedparser
from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)

RSS_FEEDS = {'bbc':'https://feeds.bbci.co.uk/news/rss.xml',
		'cnn':'http://rss.cnn.com/rss/edition.rss',
		'iol':'https://rss.iol.io/iol/news',
		'fox':'http://feeds.foxnews.com/foxnews/latest',
		'reddit':'https://reddit.com/r/worldnews/.rss',
		'de':'feeds.feedburner.com/daily-express-world-news',
		'spain':'https://feeds.thelocal.com/rss/es',
		'world':'https://world.wng.org/taxonomy/term/72/feed',
		'patriot':'https://patriotrising.com/feed',
		'btc':'https://medium.com/feed/the-capital'}

@app.route("/")
def get_news():
	query = request.args.get("publication")
	if not query or query.lower() not in RSS_FEEDS:
		publication = "bbc"
	else:
		publication  = query.lower()

	feed=feedparser.parse(RSS_FEEDS[publication])
	weather = get_weather("Carbis Bay")
	return  render_template("home.html", articles=feed['entries'], weather=weather)

def get_weather(city):
	api_key = "e3c9be28afcfde329e3380cb81c88742"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
#	city_name = "Carbis Bay"
	Final_Url = base_url + "appid=" + api_key + "&q=" +  city
	weather_data = requests.get(Final_Url).json()
	weather = None
	if weather_data.get("weather"):
		weather = {"description":weather_data["weather"][0]["description"],"temperature":weather_data["main"]["temp"],"city":weather_data["name"]}
	return weather

if __name__ == '__main__':
        app.run()
