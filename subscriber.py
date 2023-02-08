from concurrent.futures import TimeoutError
from decouple import config
from google.cloud import pubsub_v1

project_id = config('PROJECT_ID')
topic_id = config('TOPIC_ID')
sub_id = config('SUB_ID')

timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()

subscription_path = subscriber.subscription_path(project_id, sub_id)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
  print(f"Received {message}")
  message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

with subscriber:
  try:
    streaming_pull_future.result(timeout=timeout)
  except TimeoutError:
    streaming_pull_future.cancel()
    streaming_pull_future.result()