# RSS News Classifier

## Overview

This project collects news articles from various RSS feeds, classifies them into predefined categories, and stores them in a PostgreSQL database. The classification is performed using a rule-based approach powered by spaCy. A Celery task queue manages the asynchronous processing of articles. A Streamlit web app allows you to interact with the system and view articles by category.

## Setup

### Requirements

- Python 3.9
- PostgreSQL
- Redis

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Aneesahmad882/rss_news_classifier.git
    cd rss_news_classifier
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up PostgreSQL and create the database:

    ```bash
    psql -U username -c "CREATE DATABASE news_db;"
    ```

5. Set up Redis:

    ```bash
    redis-server
    ```

6. Run the Celery worker:

    ```bash
    celery -A app.tasks worker --loglevel=info
    ```

7. Run the Streamlit app:

    ```bash
    streamlit run streamlit_app.py
    ```

## Usage

1. Open the Streamlit app in your browser and trigger the pipeline to process articles.
2. View articles by selecting a category from the dropdown menu.
3. Explore the articles displayed in the data table.

## Deliverables

- **Python code** for the ETL pipeline, task queue, and Streamlit app.
- **Documentation** explaining the logic and design choices.
- **Data** in CSV and SQL dump formats.

