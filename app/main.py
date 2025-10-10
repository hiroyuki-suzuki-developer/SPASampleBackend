from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import users
from router import auth
from dotenv import load_dotenv

# env追加
load_dotenv()

app = FastAPI()

origins = ["http://localhost:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(auth.router)
