from fastapi import APIRouter

from .test import testRouter
IsmailRouters = APIRouter(prefix="/api/v1")
IsmailRouters.include_router(testRouter)
