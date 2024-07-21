import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class ENV(BaseSettings):
    db_username: str = os.getenv("DB_USERNAME")
    db_host: str = os.getenv("DB_HOST")
    db_password: str = os.getenv("DB_PASSWORD")
    auth0_secret: str = os.getenv("AUTH0_SECRET")
    auth0_client_secret: str = os.getenv("AUTH0_CLIENT_SECRET")
    auth0_domain: str = os.getenv("AUTH0_DOMAIN")
    auth0_backend_base_url: str = os.getenv("AUTH0_BACKEND_BASE_URL")
    auth0_client_id: str = os.getenv("AUTH0_CLIENT_ID")
    auth0_issuer_base_url: str = os.getenv("AUTH0_ISSUER_BASE_URL")
    auth0_api_identifier: str = os.getenv("AUTH0_API_IDENTIFIER")
    frontend_base_url: str = os.getenv("FRONTEND_BASE_URL")

load_dotenv()
env = ENV()
