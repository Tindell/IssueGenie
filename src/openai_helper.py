import os
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

def process_issue(issue_data, repo_data, user_data, mock_openai):
    if mock_openai:
        summary = "This is a mocked summary of the issue."
    else:
        summary = get_issue_summary(issue_data, repo_data, user_data)

    # TODO: Implement generating modifications based on the summary
    print(summary)
    return []

def get_issue_summary(issue_data, repo_data, user_data):
    prompt = f"Please provide a summary of the following issue:\n\nIssue title: {issue_data['title']}\nIssue body: {issue_data['body']}\nCreated by: {user_data['login']}\nRepository: {repo_data['full_name']}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant that provides concise and informative summaries of GitHub issues, including the issue title, issue body, creator, and repository. Your goal is to help developers understand the main points of an issue quickly."},
            {"role": "user", "content": prompt}
        ]
    )

    summary = response.choices[0].message['content'].strip()
    return summary

