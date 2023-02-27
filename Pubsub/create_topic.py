from google.cloud import pubsub_v1
from decouple import config

project_id = config('PROJECT_ID')
topic_id = "ATT_NEWJOIN1"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

topic = publisher.create_topic(request={"name": topic_path})

print(f"Created topic: {topic.name}")