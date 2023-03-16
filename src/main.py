import sys
from flask import Flask, request
from github_helper import create_new_branch, apply_modifications, create_pull_request
from openai_helper import process_issue

app = Flask(__name__)

mock_openai = '--mock-openai' in sys.argv

@app.route("/webhook", methods=["POST"])
def webhook():
    # Verify the webhook payload
    data = request.json
    if data.get("action") != "opened":
        return "Ignoring non-opened issue event", 200

    # Process issue information
    issue_data = data.get("issue")
    repo_data = data.get("repository")
    user_data = data.get("sender")

    print(f"issue: {issue_data} repo: {repo_data} usr: {user_data}")

    # Use OpenAI API to modify the repository based on the issue's information
    modifications = process_issue(issue_data, repo_data, user_data, mock_openai)

    # Create a new branch, apply modifications, and submit a pull request
    new_branch_name = f"issue-{issue_data['number']}-modifications"
    create_new_branch(repo_data, new_branch_name)
    apply_modifications(repo_data, new_branch_name, modifications)
    create_pull_request(repo_data, new_branch_name, issue_data)

    return "Processed issue event", 200

if __name__ == "__main__":
    app.run(debug=True)