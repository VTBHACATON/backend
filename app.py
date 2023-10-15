from fastapi import FastAPI
from backend.routers.azreil import AzreilRouters
from backend.routers.ismail import IsmailRouters
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
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


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="WEB VTB",
        version="0.1.0",
        summary="API для карты офисов и терминалов банка ВТБ",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/VTB_Logo_2018.svg/1280px-VTB_Logo_2018.svg.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


app.include_router(AzreilRouters)
app.include_router(IsmailRouters)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
