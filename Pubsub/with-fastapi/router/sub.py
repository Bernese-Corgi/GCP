from fastapi import APIRouter


router = APIRouter()

@router.get(
    path="/push/1",
    tags=['push']
)
async def push_endpoint_1():
    print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨\
          \nHi! I'm push endpoint api - sub1.\
          \nSeeing that you met me, you succeeded in your mission!\
          \n✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")