from api import app
import json


def test_api_response_format():
    client = app.test_client()
    payload = {
        "dopamine": 35,
        "serotonin": 60,
        "oxytocin": 40,
        "cortisol": 10,
        "norepinephrine": 20
    }
    response = client.post('/infer', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert 'emotion' in data
    assert 'confidence' in data
    assert 'description' in data

