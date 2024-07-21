from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from app.core.config import env
from app.utils.utils import DAY
from app.core.config import env
from app.utils.constants import oauth
from authlib.integrations.starlette_client import OAuth


def auth0_redirect(request: Request, response: Response, session: dict):
    token = session.get("id_token")
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")

    response.set_cookie(key="accessToken", value=token,
                        max_age=DAY, httponly=True, samesite="none", secure=True)
    return RedirectResponse(url=f"{env.frontend_base_url}/profile")


def register_auth0(app: FastAPI):
    global oauth

    oauth.register(
        name="auth0",
        client_id=env.auth0_client_id,
        client_secret=env.auth0_client_secret,
        client_kwargs={
            "scope": "openid",
        },
        server_metadata_url=f'https://{env.auth0_domain}/.well-known/openid-configuration',
    )


def oauth_validation_middleware():
    global oauth

    if (oauth != None):
        return True
    return False
