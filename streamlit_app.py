import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import NewsArticle
from app.tasks import process_articles
import pandas as pd

# Set up database connection
engine = create_engine('postgresql://username:password@localhost/news_db')
Session = sessionmaker(bind=engine)
session = Session()

# Function to display articles by category
def get_articles_by_category(category):
    """Fetch articles from the database by category"""
    articles = session.query(NewsArticle).filter_by(category=category).all()
    return articles

# Streamlit UI
st.title("News Article Classifier")

# Trigger ETL Pipeline
if st.button("Process Latest Articles"):
    st.write("Processing articles...")
    process_articles.delay()  # Asynchronous ETL pipeline
    st.success("Articles have been processed!")

# Display articles by category
st.header("Browse Articles by Category")
categories = ["Terrorism / protest / political unrest / riot", "Positive/Uplifting", "Natural Disasters", "Others"]
selected_category = st.selectbox("Select Category", categories)

# Fetch and display articles
if selected_category:
    articles = get_articles_by_category(selected_category)
    
    if articles:
        data = [{
            "Title": article.title,
            "Summary": article.summary,
            "Published Date": article.published,
            "Source": article.source,
            "Category": article.category
        } for article in articles]
        
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.write("No articles found.")
