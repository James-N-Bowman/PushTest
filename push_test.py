import requests
import os

response = requests.post("https://api.pushover.net/1/messages.json", data={
    "token": os.environ['PUSH_API_TOKEN'],
    "user": os.environ['PUSH_USER_KEY'], 
    "message": "Test notification from Python",
    "priority": 2,  # Emergency - will make noise until acknowledged
    "retry": 30,
    "expire": 300  # 5 minutes for testing
})

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
