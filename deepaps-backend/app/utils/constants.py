from authlib.integrations.starlette_client import OAuth
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from uuid import UUID
from pydantic import BaseModel

oauth = OAuth()


class SessionData(BaseModel):
    state: str


# Configuration for session cookies
cookie_params = CookieParameters()

cookie = SessionCookie(
    cookie_name="session",
    identifier="auth0_verifier",
    auto_error=True,
    secret_key="your_secret_key",
    cookie_params=cookie_params,
)

# In-memory backend for session data
backend = InMemoryBackend[UUID, SessionData]()

# Verifier to check session validity


class Auth0Verifier(SessionVerifier[UUID, SessionData]):
    def __init__(self, *, identifier: str, auto_error: bool, backend: InMemoryBackend[UUID, SessionData]):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    def verify_session(self, model: SessionData) -> bool:
        return True


verifier = Auth0Verifier(identifier="auth0_verifier",
                         auto_error=True, backend=backend)
