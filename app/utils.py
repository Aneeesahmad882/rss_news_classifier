import feedparser
import hashlib

feeds = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

def hash_article(article):
    """ Generate a unique hash for each article based on its URL """
    return hashlib.sha256(article['link'].encode('utf-8')).hexdigest()

def fetch_articles():
    """ Fetch articles from RSS feeds and return them as a list """
    articles = []
    for feed_url in feeds:
        parsed_feed = feedparser.parse(feed_url)
        for entry in parsed_feed.entries:
            article = {
                'title': entry.title,
                'link': entry.link,
                'summary': entry.summary,
                'published': entry.published,
                'source': feed_url,
                'hash': hash_article(entry)
            }
            articles.append(article)
    return articles
