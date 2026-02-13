from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import time

app = Flask(__name__)

# Retry until Kafka is ready
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers="kafka:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        print("Connected to Kafka")
        break
    except Exception as e:
        print(f"Kafka not ready, retrying... ({e})")
        time.sleep(3)

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    producer.send("feedback-topic", value=data)
    return jsonify({"status": "sent"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
