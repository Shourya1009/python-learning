# requests_demo.py
import requests

# Common headers
HEADERS = {
    "User-Agent": "Python Requests Demo",
    "Accept": "application/json"
}


def get_github_user(username):
    """Fetch GitHub user details"""
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()   # Raises error for bad status codes

        data = response.json()
        print("\n✅ GitHub User Found!")
        print("👤 Name:", data.get("name"))
        print("🏢 Company:", data.get("company"))
        print("🌍 Location:", data.get("location"))
        print("👥 Followers:", data.get("followers"))

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching GitHub user:", e)


def send_post_request():
    """Send POST request with JSON data"""
    url = "https://httpbin.org/post"
    payload = {
        "username": "shourya",
        "role": "developer"
    }

    try:
        response = requests.post(url, json=payload, headers=HEADERS, timeout=5)
        print("\n📤 POST Response Status:", response.status_code)
        print("Response Data:", response.json()["json"])

    except requests.exceptions.RequestException as e:
        print("❌ POST request failed:", e)


def send_put_request():
    """Update data using PUT request"""
    url = "https://httpbin.org/put"
    update_data = {
        "username": "shourya",
        "role": "senior developer"
    }

    try:
        response = requests.put(url, json=update_data, headers=HEADERS, timeout=5)
        print("\n✏️ PUT Response Status:", response.status_code)
        print("Updated Data:", response.json()["json"])

    except requests.exceptions.RequestException as e:
        print("❌ PUT request failed:", e)


def send_delete_request():
    """Delete request example"""
    url = "https://httpbin.org/delete"

    try:
        response = requests.delete(url, headers=HEADERS, timeout=5)
        print("\n🗑 DELETE Response Status:", response.status_code)
        print("Message: Resource deleted successfully (simulated)")

    except requests.exceptions.RequestException as e:
        print("❌ DELETE request failed:", e)


# Main execution
if __name__ == "__main__":
    get_github_user("octocat")
    send_post_request()
    send_put_request()
    send_delete_request()