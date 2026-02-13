FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader vader_lexicon

COPY . .

CMD ["python", "worker.py"]
