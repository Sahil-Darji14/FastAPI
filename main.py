from fastapi import FastAPI
from routers.ProductRouter import router


app = FastAPI()


app.include_router(router)