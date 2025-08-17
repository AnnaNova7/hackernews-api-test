import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def test_top_stories_not_empty():
    response = requests.get(f"{BASE_URL}/topstories.json")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], int)

# Edge case: response structure
def test_top_stories_limit_length():
    response = requests.get(f"{BASE_URL}/topstories.json")
    data = response.json()
    assert len(data) < 1000  # sanity check, should not return absurdly large list

