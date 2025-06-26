# Kafka Weather Stream

A Kafka-based micro-project that simulates weather events using real-world data and visualizes event type frequency in real time using matplotlib.

This was created as part of my 9-micro projects plan to sharpen my data engineering skills

**Feel free to check out [my Medium blog related to this project](https://smirithika.medium.com/streaming-real-time-weather-events-with-kafka-try-within-a-day-micro-project-1-13f04ac70384) for a better understanding of the process and motivation**

## Features
- Kafka producer streams weather events from JSONL
- Kafka consumer logs and plots live event type frequency
- Dockerized Kafka & Zookeeper setup
- Modular logging and chart saving

## Requirements
- Python 3.10+
- Docker
- matplotlib, kafka-python, pandas

## Dataset 
Kaggle - US Weather Events (2016–2022)
https://www.kaggle.com/datasets/sobhanmoosavi/us-weather-events

## Run
```bash
docker-compose -f docker/docker-compose.yml up -d
python scripts/convert_csv_to_jsonl.py
python scripts/producer.py
python scripts/consumer.py
