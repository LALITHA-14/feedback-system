import time
import json
from kafka import KafkaConsumer

print("Worker started...")

while True:
    try:
        print("Connecting to Kafka...")
        consumer = KafkaConsumer(
            'feedback',
            bootstrap_servers='kafka:9092',
            auto_offset_reset='earliest',
            group_id="worker-group",
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        print("Connected to Kafka!")
        break
    except Exception as e:
        print("Kafka not ready, retrying...", e)
        time.sleep(5)

print("Waiting for messages...")

for message in consumer:
    print("Received:", message.value)