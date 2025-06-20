import json
import time
import logging
from kafka import KafkaProducer

logging.basicConfig(
    filename='logs/producer.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Initializing KafkaProducer")
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'weather_events'
input_file = 'data/weather_events.jsonl'

with open(input_file, 'r') as file:
    for i, line in enumerate(file):
        try:
            event = json.loads(line.strip())
            logging.info(f"Sending event {i + 1}: {event}")
            producer.send(topic, value=event)
            time.sleep(2) # Simulate a delay between messages
        except Exception as e:
            logging.error(f"Failed to send event on line {i + 1}: {e}")

producer.flush()
producer.close()
logging.info("All events sent to Kafka topic.")



