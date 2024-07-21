from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes.users import users_router
from app.routes.auth0 import auth0_router
from app.services.auth0 import register_auth0
from app.core.config import env
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import uvicorn



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key=env.auth0_secret)

register_auth0(app)

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(auth0_router, prefix="/auth0", tags=["auth0"])


@app.get("/test")
def test():
    return "Test"


@app.get("/")
async def read_root():
    return RedirectResponse(url="/test")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)