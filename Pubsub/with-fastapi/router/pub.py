from fastapi import APIRouter, Depends

from client import PubsubClient


router = APIRouter()

@router.get(
    path="/",
)
async def publish_msg():
    pubsub = PubsubClient()
    pub = pubsub.publisher

    result = pub.publish(
        topic=pubsub.one_topic_path,
        data=b"hi"
    )
    
    print(result)
