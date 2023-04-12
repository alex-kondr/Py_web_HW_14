import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
import uvicorn
import redis.asyncio as redis

from src.routes import contacts, auth, groups, user
from src.conf.config import settings


app = FastAPI()


@app.on_event("startup")
async def startup():
    """
    The startup function is called when the application starts up.
    It's a good place to initialize things that are needed by your app, such as databases or caches.

    :return: A coroutine, which is a function that returns
    """
    r = await redis.Redis(host=settings.redis_host,
                          port=settings.redis_port,
                          password=settings.redis_password,
                          encoding="utf-8",
                          decode_responses=True)
    await FastAPILimiter.init(r)

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    The add_process_time_header function is a middleware function that adds the time it took to process
    the request in seconds as a header called Process-Time. This can be useful for debugging purposes.

    :param request: Request: Get the request object
    :param call_next: Call the next middleware in the chain
    :return: A response object with a header
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["Process-Time"] = str(process_time)
    return response


app.include_router(contacts.router, prefix="/api")
app.include_router(groups.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(user.router, prefix="/api")


@app.get("/healthchecker")
def read_root():
    """
    The read_root function returns a dictionary with the key message and value Hello world!.

    :return: A dictionary with a single key, message
    """
    return {"message": "Hello world!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
