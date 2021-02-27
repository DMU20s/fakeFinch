from typing import Optional
from fastapi import FastAPI
from random import seed
from random import random
import time

app = FastAPI()


@app.get("/")
def read_root():
	return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
	return {"item_id": item_id, "q": q}


@app.get("/dummytal/get")
def give_dummy_data():
	print(time.time())
	seed(1)
	print(random())
	return {str(time.time()): str(random())}
