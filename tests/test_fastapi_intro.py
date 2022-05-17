from fastapi_intro import __version__
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_version():
    assert __version__ == '0.1.0'

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
