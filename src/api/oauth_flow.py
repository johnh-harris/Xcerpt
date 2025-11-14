import base64, hashlib, os
from urllib.parse import urlencode
from dotenv import load_dotenv
import os
import requests

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

def generate_pkce():
    verifier = base64.urlsafe_b64encode(os.urandom(40)).rstrip(b'=').decode('utf-8')
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode('utf-8')).digest()
    ).rstrip(b'=').decode('utf-8')
    return verifier, challenge

verifier, challenge = generate_pkce()

def build_login_url():
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "tweet.read users.read offline.access",
        "state": "xyz123",
        "code_challenge": challenge,
        "code_challenge_method": "S256"
    }
    return "https://twitter.com/i/oauth2/authorize?" + urlencode(params)


def exchange_code_for_token(code):
    token_url = "https://api.x.com/oauth2/token"

    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "code": code,
        "code_verifier": verifier
    }

    response = requests.post(token_url, data=data)
    return response.json()