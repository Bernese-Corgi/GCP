from google.cloud import pubsub_v1
from decouple import config

project_id = config('PROJECT_ID')
topic_id = config('TOPIC_ID')

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 10):
  data_str = f"Message number {n}"
  data = data_str.encode('utf-8')
  future = publisher.publish(topic_path, data)
  print(future.result())

print(f"Published message to {topic_path}.")