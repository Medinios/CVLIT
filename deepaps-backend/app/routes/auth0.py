from urllib.parse import quote_plus, urlencode
from uuid import UUID, uuid4
from fastapi import APIRouter, HTTPException, Request, Response, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse
from app.core.config import env
from app.services.auth0 import oauth_validation_middleware
from app.utils.constants import SessionData, oauth, backend, cookie

auth0_router = APIRouter()


@auth0_router.get("/login")
async def auth0_login(request: Request, response: Response, valid=Depends(oauth_validation_middleware)):
    global oauth
    global backend
    global cookie

    if not valid:
        raise HTTPException(
            status_code=500, detail="OAuth not configured properly")
    state = uuid4().hex
    session_id = uuid4()
    data = SessionData(state=state)

    await backend.create(session_id, data)
    cookie.attach_to_response(response, session_id)

    return await oauth.auth0.authorize_redirect(request, redirect_uri=request.url_for("callback"), state=state)


@auth0_router.route("/callback", methods=["GET", "POST"], name="callback")
async def auth0_login_callback(request: Request):
    global oauth
    global backend
    global cookie

    session_id_str = request.cookies.get("session")
    if not session_id_str:
        raise HTTPException(status_code=400, detail="Missing session ID")

    try:
        session_id = UUID(cookie.decode(session_id_str))
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Invalid session ID format")

    session_data = await backend.read(session_id)

    state_sent = request.query_params.get('state')
    state_stored = session_data.state

    if state_stored != state_sent:
        raise HTTPException(status_code=400, detail="Mismatching state")

    token = await oauth.auth0.authorize_access_token(request)
    request.session["user"] = jsonable_encoder(token)

    return RedirectResponse("/")


@auth0_router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    logout_url = (
        f"https://{env.auth0_domain}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.url_for("read_root", _external=True),
                "client_id": env.auth0_client_id,
            },
            quote_via=quote_plus,
        )
    )
    return RedirectResponse(url=logout_url)
