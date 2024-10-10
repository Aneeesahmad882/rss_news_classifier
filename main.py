from app.tasks import process_articles

# Trigger the processing of articles
if __name__ == '__main__':
    process_articles.delay()
