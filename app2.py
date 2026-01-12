import fastapi
from fastapi import FastAPI
from login import router as Loginrouter
from news import router as Newsrouter
from notice import router as Noticerouter


app = FastAPI()

app.include_router(Loginrouter)
app.include_router(Newsrouter)
app.include_router(Noticerouter)






