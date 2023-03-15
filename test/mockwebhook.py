import json
import requests

# TODO I didn't check this against github docs.  It is just ChatGPT generarted

def send_mock_payload(url, payload):
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.text, response.status_code

if __name__ == "__main__":
    # Replace this URL with your local server URL (e.g., "http://localhost:5000/webhook")
    webhook_url = "http://127.0.0.1:5000/webhook"

    # Define a sample GitHub webhook payload (you can replace this with any sample payload)
    mock_payload = {
        "action": "opened",
        "issue": {
            "number": 123,
            "title": "Sample issue",
            "body": "This is a sample issue for testing the webhook."
        },
        "repository": {
            "full_name": "yourusername/yourrepository",
            "default_branch": "main"
        },
        "sender": {
            "login": "yourusername"
        }
    }

    response_text, status_code = send_mock_payload(webhook_url, mock_payload)
    print(f"Response status code: {status_code}\nResponse text: {response_text}")
