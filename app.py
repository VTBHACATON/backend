from fastapi import FastAPI
from routers.azreil import AzreilRouters
from routers.ismail import IsmailRouters
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


app.include_router(AzreilRouters)
app.include_router(IsmailRouters)
