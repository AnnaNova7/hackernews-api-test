import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def test_first_comment_of_top_story():
    # Happy path
    top_story = requests.get(f"{BASE_URL}/topstories.json").json()[0]
    story = requests.get(f"{BASE_URL}/item/{top_story}.json").json()
    first_comment_id = story.get("kids", [])[0]
    comment = requests.get(f"{BASE_URL}/item/{first_comment_id}.json").json()
    
    assert "id" in comment
    assert "by" in comment
    assert "text" in comment or comment.get("deleted", False)  # Some comments are deleted

# Negative case: comment ID that doesn’t exist
def test_invalid_comment():
    response = requests.get(f"{BASE_URL}/item/0.json")
    assert response.status_code == 200
    assert response.json() in [None, {}]

