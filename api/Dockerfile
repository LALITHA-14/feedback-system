FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask kafka-python

CMD ["python", "api.py"]