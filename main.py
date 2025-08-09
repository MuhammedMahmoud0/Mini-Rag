from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
    <h1>HELLO WORLD</h1>
    <a href="/welcome">welcome</a>
"""


@app.get("/welcome")
def welcome():
    return {"message": "hello world"}


@app.get("/", response_class=HTMLResponse)
def home():
    return html
