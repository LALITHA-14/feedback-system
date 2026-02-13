from flask import Flask, request, jsonify
from kafka import KafkaProducer
import uuid
import json
import os
from datetime import datetime

app = Flask(__name__)
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'kafka:9092')

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    if not all(k in data for k in ['customer_id', 'feedback_text', 'timestamp']):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
    except ValueError:
        return jsonify({'error': 'Invalid timestamp format'}), 400

    message_id = str(uuid.uuid4())
    feedback_event = {
        'message_id': message_id,
        'customer_id': data['customer_id'],
        'feedback_text': data['feedback_text'],
        'feedback_timestamp': data['timestamp']
    }

    producer.send('customer_feedback_events', feedback_event)
    producer.flush()

    return jsonify({'message': 'Feedback received for processing', 'message_id': message_id}), 202

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
