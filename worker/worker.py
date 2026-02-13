from kafka import KafkaConsumer
import json

# Create the Kafka consumer
consumer = KafkaConsumer(
    'feedback',                               # topic name
    bootstrap_servers='feedback-system-kafka-1:9092',  # Docker Kafka service
    group_id='feedback-group',                # consumer group
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),  # decode JSON
    auto_offset_reset='earliest'              # read from beginning if no offset
)

print("Worker started, waiting for messages...")

# Consume messages
for message in consumer:
    print("Received:", message.value)
