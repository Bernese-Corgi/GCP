from decouple import config
from google.cloud import pubsub_v1

project_id = config('PROJECT_ID')
# topic_id = config('TOPIC_ID')
newjoin_rule_type = config('NEWJOIN_ID')
sub_id = config('SUB_ID')

subscriber = pubsub_v1.SubscriberClient()
sub_path = subscriber.subscription_path(project_id, sub_id)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
  encoding = message.attributes.get('')