from flask import Flask, request
from kafka import KafkaProducer
import time
import json

app = Flask(__name__)

# Retry Kafka connection
while True:
    try:
        print("Connecting to Kafka...")
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Connected to Kafka!")
        break
    except Exception as e:
        print("Kafka not ready, retrying...", e)
        time.sleep(5)

@app.route("/")
def home():
    return "API is running!"

@app.route("/send", methods=["POST"])
def send():
    try:
        data = request.get_json(force=True)

        if "message" not in data:
            return {"error": "No message provided"}, 400

        producer.send("feedback", {"message": data["message"]})
        producer.flush()

        return {"status": "Message sent!"}

    except Exception as e:
        print("ERROR:", e)
        return {"error": "Failed to send"}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)