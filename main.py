from fastapi import FastAPI
from Router.ProductRouter import router

app = FastAPI()

app.include_router(router)