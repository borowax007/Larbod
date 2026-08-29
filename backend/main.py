from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from schemas import ContactCreate

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel, EmailStr, Field


# Project root: Larbod/
BASE_DIR = Path(__file__).resolve().parent.parent


app = FastAPI(title="Larbod")


# Serve the assets folder
app.mount(
    "/assets",
    StaticFiles(directory=BASE_DIR / "assets"),
    name="assets"
)


# Serve the Larbod website
@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


# Serve CSS
@app.get("/style.css")
def style():
    return FileResponse(BASE_DIR / "style.css")


# Serve JavaScript
@app.get("/script.js")
def script():
    return FileResponse(BASE_DIR / "script.js")


# Receive contact form
@app.post("/contact")
def create_contact(contact: ContactCreate):

    print("New contact message:")
    print(contact)

    return {
        "message": "Contact message received",
        "data": contact
    }