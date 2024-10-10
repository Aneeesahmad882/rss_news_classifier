from celery import Celery
from app.utils import fetch_articles
from app.models import session, NewsArticle
import spacy
from sqlalchemy.exc import IntegrityError

app = Celery('app', broker='redis://localhost:6380/0')
app.config_from_object('celeryconfig')

# Load spaCy model for NLP
nlp = spacy.load("en_core_web_sm")

@app.task
def classify_article(article):
    """ Classify articles based on their content """
    doc = nlp(article['summary'])
    
    if any(word in doc.text.lower() for word in ["terrorism", "protest", "riot", "unrest"]):
        category = "Terrorism / protest / political unrest / riot"
    elif any(word in doc.text.lower() for word in ["disaster", "earthquake", "flood", "hurricane"]):
        category = "Natural Disasters"
    elif any(word in doc.text.lower() for word in ["happy", "success", "positive", "uplifting"]):
        category = "Positive/Uplifting"
    else:
        category = "Others"
    
    return category

@app.task
def process_articles():
    """ Fetch and classify articles, then store them in the database """
    articles = fetch_articles()
    
    for article in articles:
        category = classify_article(article)
        article['category'] = category
        
        news = NewsArticle(
            id=article['hash'],
            title=article['title'],
            link=article['link'],
            summary=article['summary'],
            published=article['published'],
            source=article['source'],
            category=article['category']
        )
        
        try:
            session.add(news)
            session.commit()
        except IntegrityError:
            session.rollback()  # Handle duplicate entries
