from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr, Field

from routers import contacts

# Project root: Larbod/
BASE_DIR = Path(__file__).resolve().parent.parent


app = FastAPI(title="Larbod")
app.include_router(contacts.router)

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