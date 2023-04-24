from fastapi import FastAPI


def start_server():
    app = FastAPI()
    
    # app.include_router()
    
    return app

app = start_server()