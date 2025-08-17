# HackerNews API Test Suite
This repository contains automated tests for the [HackerNews API](https://github.com/HackerNews/API).  
It validates API functionality, covers edge cases, and documents bugs found.

## 📦 Setup
```bash
Clone the repository:
   git clone https://github.com/your-username/hackernews-api-test.git
   cd hackernews-api-test
Create and activate a virtual environment:
    python3 -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
Install dependencies:
    pip install -r requirements.txt
Running Tests:
    pytest -v
Run with coverage:
    pytest --cov=tests -v
```

✅ Test Coverage
# The suite covers:
Top Stories
- Ensures the list of stories is not empty
- Validates that limiting the number of results works
Items
- Fetches a valid item
- Handles invalid IDs (negative, string, large numbers)
- Handles nonexistent IDs
Comments
- Retrieves the first comment of a top story
- Handles invalid or missing comment IDs
Reliability
- Handles multiple rapid requests consistently (load testing)
- Validates schema on repeated calls

Result:
✅ 13 tests executed successfully  
✅ 100% test coverage across all modules 

🔍 Edge Cases Tested:
Invalid IDs (-1, "abc", very large number)
Nonexistent items (API returns null instead of error)
Empty/invalid comment parent IDs
Top stories exceeding limit length
Multiple back-to-back API calls

🐞 Bugs Found:
Inconsistent error handling:
- The API sometimes returns 200 OK with null instead of 404 Not Found.
Example: invalid item IDs.
Comments edge case:
- Invalid comment IDs also return null without an error, making it hard for clients to distinguish between “no comment” and “bad input.”

## 🔄 CI
Tests run automatically on each push using GitHub Actions (.github/workflows/tests.yml).
