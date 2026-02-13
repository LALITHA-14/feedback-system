\# Event-Driven Feedback Analysis System



An event-driven microservices application that processes customer feedback using Kafka and performs sentiment analysis before storing results in MySQL.



\## 📌 Architecture Overview



This project uses:



\- \*\*Kafka\*\* – Event streaming platform

\- \*\*MySQL\*\* – Database for storing analysis results

\- \*\*API Service\*\* – Produces feedback events to Kafka

\- \*\*Worker Service\*\* – Consumes events, performs sentiment analysis, stores results

\- \*\*Docker Compose\*\* – Container orchestration





\## 🏗️ System Flow



1\. Client sends feedback to the API.

2\. API publishes feedback event to Kafka topic.

3\. Worker consumes event from Kafka.

4\. Sentiment analysis is performed.

5\. Result is stored in MySQL.





\## 📂 Project Structure



```



feedback-system/

│   .env.example

│   cd

│   docker

│   docker-compose.yml

│   README.md

│

├───api

│       app.py

│       Dockerfile

│       requirements.txt

│

├───db

│       init.sql

│

├───tests

└───worker

&nbsp;       Dockerfile

&nbsp;       requirements.txt

&nbsp;       worker.py

````



\## ⚙️ Prerequisites



\- Docker

\- Docker Compose





\## 🚀 Setup Instructions



\### 1️⃣ Clone the repository



```bash

git clone <repository-url>

cd event-driven-feedback

````



\### 2️⃣ Start the application



```bash

docker-compose down -v

docker-compose up --build

```



To run in detached mode:



```bash

docker-compose up --build -d

```



\## 🌐 Services



| Service | Port | Description                      |

| ------- | ---- | -------------------------------- |

| API     | 5000 | REST API for feedback submission |

| Kafka   | 9092 | Message broker                   |

| MySQL   | 3306 | Database                         |





\## 📨 Example API Request



```bash

POST http://localhost:5000/feedback

```



Example JSON:



```json

{

&nbsp; "message\_id": "msg123",

&nbsp; "customer\_id": "cust1",

&nbsp; "feedback\_text": "The product quality is excellent!",

&nbsp; "feedback\_timestamp": "2026-02-13T10:00:00"

}

```



\## 🧠 Sentiment Analysis



The worker performs sentiment classification using the `analyze()` function in:



```

worker/sentiment.py

```



Possible outputs:



\* Positive

\* Negative

\* Neutral





\## 🗄️ Database Table



`feedback\_analysis`



| Column             | Description          |

| ------------------ | -------------------- |

| message\_id         | Unique feedback ID   |

| customer\_id        | Customer identifier  |

| feedback\_text      | Original feedback    |

| sentiment          | Sentiment result     |

| feedback\_timestamp | Original timestamp   |

| processed\_at       | Processing timestamp |



---



\## 🔍 Viewing Logs



```bash

docker-compose logs -f

```



Specific service:



```bash

docker-compose logs -f worker

```



\## 🛑 Stopping the Application



```bash

docker-compose down

```



To remove volumes:



```bash

docker-compose down -v

```





\## 🛠️ Environment Variables



Defined in `.env.example`:



```

KAFKA\_BROKER=kafka:9092

KAFKA\_TOPIC=customer\_feedback\_events



MYSQL\_HOST=mysql

MYSQL\_USER=root

MYSQL\_PASSWORD=root\_password

MYSQL\_DATABASE=feedback\_db

```



\## 👩‍💻 Author



Pullela Lalitha

