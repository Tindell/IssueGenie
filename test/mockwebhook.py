import json
import requests

def send_mock_payload(url):
    with open('test/mock-hook.json', 'r') as file:
        payload = json.load(file)

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.text, response.status_code

if __name__ == "__main__":
    # Replace this URL with your local server URL (e.g., "http://localhost:5000/webhook")
    webhook_url = "http://127.0.0.1:5000/webhook"

    response_text, status_code = send_mock_payload(webhook_url)
    print(f"Response status code: {status_code}\nResponse text: {response_text}")