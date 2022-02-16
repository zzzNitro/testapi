import json
from fastapi import FastAPI
import requests

app = FastAPI()

url = "https://rickandmortyapi.com/api/character"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
characters = response.json()

@app.get("/")
def index():
    return {"home": "sin datos"}

@app.get("/characters")
def get_characters(species: str, gender: str | None = None):
    if gender:
        return characters
    return characters