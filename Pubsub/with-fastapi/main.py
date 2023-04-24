from fastapi import FastAPI

from router import pub


def start_server():
    app = FastAPI()
    
    app.include_router(
        router=pub.router,
        prefix="/pub",
        tags=["publish"],
    )

    return app

app = start_server()