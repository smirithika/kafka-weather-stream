import json
import logging
from collections import Counter
from kafka import KafkaConsumer
from plot import plot_event_counts


logging.basicConfig(
    filename='logs/consumer.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

topic = 'weather_events'

logging.info("Initializing KafkaConsumer")
consumer = KafkaConsumer(
    topic,
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='weather_consumer_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

logging.info(f"\n listening for events on topic '{topic}' ...\n")

event_counts = Counter()

for i, message in enumerate(consumer):
    try:
        event = message.value
        logging.info(f"Received event {i + 1}: {event.get('EventId', '[NO-ID]')} | Type: {event.get('Type')} | City: {event.get('City')}")

        etype = event.get('Type', 'Unknown')
        event_counts[etype] += 1
        plot_event_counts(event_counts)
    except Exception as e:
        logging.error(f"Error processing message {i + 1}: {e}")