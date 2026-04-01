# Kafka Feedback System 🚀

## 📌 Overview
This project is a real-time feedback system using:

- Flask (API)
- Apache Kafka (Message Broker)
- Zookeeper
- Docker & Docker Compose

---

## ⚙️ Architecture

User → Flask API → Kafka → Consumer (Worker)

---

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/YOUR-USERNAME/feedback-system.git
cd feedback-system
```

### 2. Run Docker
```bash
docker compose up --build
```

## 🌐 API Endpoints

### 1. Home
```bash
GET /
```
Response:
```bash
API is running!
```

### Send Feedback
```bash
POST /send
Content-Type: application/json
```
Request Body:
```bash
{
  "message": "Hello Kafka"
}
```
Response:
```bash
{
  "status": "Message sent!"
}
```

## 🧪 Testing
Send message
```bash
curl -X POST http://localhost:5000/send -H "Content-Type: application/json" -d "{\"message\":\"Hello Kafka\"}"
```

Verify Kafka messages
```bash
docker exec -it feedback-system-kafka-1 kafka-console-consumer --bootstrap-server kafka:9092 --topic feedback --from-beginning
```

## 📦 Services
| Service   | Port |
| --------- | ---- |
| API       | 5000 |
| Kafka     | 9092 |
| Zookeeper | 2181 |

## 📌 Notes
- Kafka may take a few seconds to initialize
- API retries Kafka connection automatically
- Worker consumes messages from the feedback topic
- Docker Compose manages all services

## ✅ Output Example
```bash
{"message": "Hello Kafka"}
{"message": "Final Test"}
{"message": "Check"}
```



