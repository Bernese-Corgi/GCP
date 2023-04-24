import json
from os import getcwd, path
from google.cloud import pubsub_v1
from google.auth import jwt
from decouple import config


class PubsubClient:
    def __init__(self) -> None:
        base_dir = getcwd()

        with open(base_dir + "/key.json") as f:
            key = json.load(f)
        
        audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
        credentials = jwt.Credentials.from_service_account_info(
            key, audience=audience
        )
        
        self._publisher = pubsub_v1.PublisherClient(credentials=credentials)
        self._subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
        self._project_id = config('PROJECT_ID')
        self._one_topic_id = config('ONE_TOPIC_ID')
        
        print("✨✨✨✨✨ PubsubClient | __init__ ✨✨✨✨✨")
    
    @property
    def publisher(self):
        return self._publisher

    @property
    def subscriber(self):
        return self._subscriber
    
    @property
    def project_id(self):
        return self._project_id
    
    @property
    def one_topic_id(self):
        return self._one_topic_id
    
    @property
    def one_topic_path(self):
        topic_path = self.publisher.topic_path(
            project=self.project_id,
            topic=self.one_topic_id
        )
        return topic_path
    
ps_client = PubsubClient()