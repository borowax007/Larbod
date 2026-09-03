from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from routers import contacts


BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="Larbod")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts.router)

app.mount(
    "/assets",
    StaticFiles(directory=BASE_DIR / "assets"),
    name="assets"
)


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/style.css")
def style():
    return FileResponse(BASE_DIR / "style.css")


@app.get("/script.js")
def script():
    return FileResponse(BASE_DIR / "script.js")