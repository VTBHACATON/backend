from fastapi import APIRouter

from .test import testRouter
AzreilRouters = APIRouter(prefix="/api/v1")
AzreilRouters.include_router(testRouter)
