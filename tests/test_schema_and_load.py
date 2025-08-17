import pytest
import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

# ✅ Test 1: Schema Validation
def test_item_schema():
    item_id = 8863  # Known valid story
    r = requests.get(f"{BASE_URL}/item/{item_id}.json")
    assert r.status_code == 200
    data = r.json()
    # Make sure required keys exist
    for key in ["id", "type", "by"]:
        assert key in data, f"Missing key: {key}"

# ✅ Test 2: Stress Test (Basic Rate Check)
@pytest.mark.parametrize("i", range(5))
def test_multiple_requests(i):
    # send several requests quickly
    r = requests.get(f"{BASE_URL}/topstories.json")
    assert r.status_code == 200
    assert isinstance(r.json(), list)