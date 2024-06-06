from config import API_KEY, BASE_URL, USERNAME

import pytest
import requests
import base64


@pytest.fixture(scope="module")
def authenticated_session():
    session = requests.Session()
    credentials = f"{USERNAME}:{API_KEY}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    session.headers.update({
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    })
    yield session
    session.close()
