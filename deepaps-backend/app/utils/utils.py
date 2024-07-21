from app.core.config import env
from auth0.v3.authentication import GetToken

SECOND = 1000
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
YEAR = 365 * DAY


def get_jwt_bearer_token():
    domain = env.auth0_issuer_base_url
    client_id = env.auth0_client_id
    client_secret = env.auth0_secret
    audience = env.auth0_api_identifier
    get_token = GetToken(domain)
    token = get_token.client_credentials(client_id, client_secret, audience)
    return token['access_token']
