from kafka import KafkaConsumer
import json
import os
import pymysql
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime

# Kafka setup
consumer = KafkaConsumer(
    'customer_feedback_events',
    bootstrap_servers=[os.getenv('KAFKA_BROKER', 'kafka:9092')],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sentiment_analyzer_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# MySQL setup
MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'feedback_db')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'root_password')

connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE,
    autocommit=True
)

cursor = connection.cursor()

# NLTK Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

print("Worker started, waiting for messages...")

for message in consumer:
    feedback = message.value
    vs = analyzer.polarity_scores(feedback['feedback_text'])
    if vs['compound'] >= 0.05:
        sentiment = 'positive'
    elif vs['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    # Idempotent insert
    sql = """
    INSERT INTO feedback_analysis
    (message_id, customer_id, feedback_text, sentiment_score, feedback_timestamp, analysis_timestamp)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE sentiment_score=VALUES(sentiment_score), analysis_timestamp=VALUES(analysis_timestamp)
    """
    cursor.execute(sql, (
        feedback['message_id'],
        feedback['customer_id'],
        feedback['feedback_text'],
        sentiment,
        feedback['feedback_timestamp'],
        datetime.utcnow()
    ))

    print(f"Processed message {feedback['message_id']} with sentiment {sentiment}")
