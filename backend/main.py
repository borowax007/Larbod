from pathlib import Path

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


class ContactMessage(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    budget: str
    project_type: str
    message: str = Field(min_length=10, max_length=2000)


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
def create_contact(contact: ContactMessage):

    print("New contact message:")
    print(contact)

    return {
        "message": "Contact message received",
        "data": contact
    }