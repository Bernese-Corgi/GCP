from google.cloud import pubsub_v1
from decouple import config
import requests

project_id = config('PROJECT_ID')
topic_id = config('TOPIC_ID')
danaka_url = config('DANAKA_URL')
newjoin_rule_type = config('NEWJOIN_ID')

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path(project_id, topic_id)

def get_coupon_rule(rule_type):
  response = requests.get(
    f"{danaka_url}/coupon/rule",
    params={ "ruleType": rule_type }
  )
  return response.json()

coupon_rule = get_coupon_rule(newjoin_rule_type)

coupon_list = [str(rule["couponNo"]) for rule in coupon_rule]
data_str = ",".join(coupon_list)
data = data_str.encode('utf-8')

future = publisher.publish(topic_path, data)

print(future.result())