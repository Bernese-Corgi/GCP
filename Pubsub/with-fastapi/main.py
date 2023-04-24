from fastapi import FastAPI

from router import pub, sub


def start_server():
    app = FastAPI()
    
    app.include_router(
        router=pub.router,
        prefix="/pub",
        tags=["publish"],
    )

    app.include_router(
        router=sub.router,
        prefix="/sub",
        tags=["subscribe"],
    )
    
    return app

app = start_server()