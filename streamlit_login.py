import streamlit as st;
from httpx_oauth.clients.google import GoogleOAuth2
import asyncio
import webbrowser
from numpy import void
CLIENT_ID ="1047006337706-7mcl5a23hamsra16dd51ege6tia7m72m.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:8501"



async def get_authorization_url(client: GoogleOAuth2, redirect_uri: str):
    authorization_url = await client.get_authorization_url(redirect_uri, scope=["profile", "email"])
    return authorization_url

async def get_access_token(client: GoogleOAuth2, redirect_uri: str, code: str):
    token = await client.get_access_token(code, redirect_uri)
    return token
def get_login_str():
    client: GoogleOAuth2 = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
    authorization_url = asyncio.run(get_authorization_url(client, REDIRECT_URI))
    webbrowser.open_new(authorization_url);
    return f''' < a target = "_self" href = "{authorization_url}" > Google login < /a > '''

async def get_email(client: GoogleOAuth2, token: str):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email

def display_user() -> void:
    client: GoogleOAuth2 = GoogleOAuth2(CLIENT_ID, CLIENT_SECRET)
    # get the code from the url
    code = st.experimental_get_query_params()['code']

    token = asyncio.run(get_access_token(client, REDIRECT_URI, code))

    user_id, user_email = asyncio.run(get_email(client, token['access_token']))
    st.write("You're logged in as {user_email} and id is {user_id}")

# if (st.button("Using Google")):
#     st.title("Streamlit Oauth Login");
#     st.write(get_login_str(), unsafe_allow_html=True)
# if(st.button("display button")):
#     display_user();


