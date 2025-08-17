import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def test_get_item():
    # Happy path
    response = requests.get(f"{BASE_URL}/item/8863.json")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == 8863

# Negative case: invalid ID
def test_get_invalid_item():
    response = requests.get(f"{BASE_URL}/item/-1.json")
    assert response.status_code == 200
    assert response.json() in [None, {}]

# Edge case: very large ID
def test_get_nonexistent_item():
    response = requests.get(f"{BASE_URL}/item/9999999999.json")
    assert response.status_code == 200
    assert response.json() in [None, {}]

