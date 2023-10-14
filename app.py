from fastapi import FastAPI
from backend.routers.azreil import AzreilRouters
from backend.routers.ismail import IsmailRouters
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
load_dotenv()

origins = [
    "*"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(AzreilRouters)
app.include_router(IsmailRouters)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
