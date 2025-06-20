import pandas as pd
import json
import logging

logging.basicConfig(
    filename='logs/convert_csv_to_jsonl.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

csv_file_path = '/home/smirithi/projects/stream-data-analytics/data/us-weather-events/WeatherEvents_Jan2016-Dec2022.csv'
jsonl_file_path = 'data/weather_events.jsonl'

chunk_size = 10000
total_records = 0

# Convert each chunk to JSON lines format and write to file
with open(jsonl_file_path, 'w') as jsonl_file:
    for i, chunk in enumerate(pd.read_csv(csv_file_path, chunksize=chunk_size)):
        records = chunk.to_dict(orient='records')
        for record in records:
            jsonl_file.write(json.dumps(record) + '\n')
        total_records += len(records)
        logging.info(f"Processed chunk {i + 1}")
    
logging.info(f"Completed conversion to {jsonl_file_path}, total records written: {total_records}")