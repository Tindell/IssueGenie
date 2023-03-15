# IssueGenie
## Running locally
> pipenv run python src/main.py
> pipenv run python test/mockwebhook.py

## Running with ngrok
> ngrok 127.0.0.1:5000
Set up a webhook on GitHub:
Go to your repository's settings, then click "Webhooks."
Click "Add webhook."
In "Payload URL," enter the ngrok URL (e.g., https://your_ngrok_subdomain.ngrok.io/webhook).
Set "Content type" to application/json.
Select "Let me select individual events" and choose "Issues."
Save the webhook.
