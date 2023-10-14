from fastapi import FastAPI
from routers.azreil import AzreilRouters
from routers.ismail import IsmailRouters
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

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
