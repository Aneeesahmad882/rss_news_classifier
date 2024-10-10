from sqlalchemy import create_engine, Column, String, Text, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'
    id = Column(String, primary_key=True)
    title = Column(String)
    link = Column(String)
    summary = Column(Text)
    published = Column(DateTime)
    source = Column(String)
    category = Column(String)
    
    __table_args__ = (UniqueConstraint('id', name='_article_uc'),)

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:Anees@localhost/news_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()