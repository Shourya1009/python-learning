# requests_demo.py
import requests

# 1. GET request
url = "https://api.github.com/users/octocat"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("✅ User found!")
    print("👤 Name:", data.get("name"))
    print("🏢 Company:", data.get("company"))
    print("🔗 Blog:", data.get("blog"))
else:
    print("❌ Error:", response.status_code)


# 2. POST request (sending data)
url = "https://httpbin.org/post"  # Testing endpoint
payload = {"username": "shourya", "role": "developer"}
response = requests.post(url, json=payload)

print("\n📤 POST Response:")
print(response.json())


# 3. PUT request (update data)
url = "https://httpbin.org/put"
update_data = {"username": "shourya", "role": "senior developer"}
response = requests.put(url, json=update_data)

print("\n✏️ PUT Response:")
print(response.json())


# 4. DELETE request
url = "https://httpbin.org/delete"
response = requests.delete(url)

print("\n🗑 DELETE Response:")
print(response.json())
