import imp
import json
import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse
from zipfile import ZipFile


app = FastAPI()

url = "https://rickandmortyapi.com/api/character"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
characters = response.json()

file_path = "all_characters.zip"

@app.get("/")
def index():
    return {"home": "sin datos"}

@app.get("/characters")
def get_characters(species: str, gender: str | None = None):
    if gender:
        return characters
    return characters

@app.get("/download")
def download_characters():
    with open('all_characters.json', 'w') as outfile:
        outfile.write(json.dumps(characters))

    with ZipFile('all_characters.zip', 'w') as download_file:
        download_file.write('all_characters.json')

    return FileResponse(path=file_path, filename=file_path)