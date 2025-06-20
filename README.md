# Kafka Weather Stream

A Kafka-based micro-project that simulates weather events using real-world data and visualizes event type frequency in real time using matplotlib.

## Features
- Kafka producer streams weather events from JSONL
- Kafka consumer logs and plots live event type frequency
- Dockerized Kafka & Zookeeper setup
- Modular logging and chart saving

## Requirements
- Python 3.10+
- Docker
- matplotlib, kafka-python, pandas

## Run
```bash
docker-compose -f docker/docker-compose.yml up -d
python scripts/convert_csv_to_jsonl.py
python scripts/producer.py
python scripts/consumer.py
