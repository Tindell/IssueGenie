import os
import requests
import base64

GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

def create_new_branch(repo_data, new_branch_name):
    default_branch = repo_data["default_branch"]
    repo_full_name = repo_data["full_name"]

    # Step 1: Retrieve the default branch's reference
    default_branch_ref_url = f"https://api.github.com/repos/{repo_full_name}/git/ref/heads/{default_branch}"
    response = requests.get(default_branch_ref_url, headers=get_github_auth_header())

    if response.status_code != 200:
        raise Exception(f"Failed to fetch default branch '{default_branch}' reference: {response.status_code} - {response.text}")

    default_branch_ref_data = response.json()
    default_branch_commit_sha = default_branch_ref_data["object"]["sha"]

    # Step 2: Create a new reference (branch) pointing to the same commit as the default branch
    new_branch_ref_url = f"https://api.github.com/repos/{repo_full_name}/git/refs"
    new_branch_ref_data = {
        "ref": f"refs/heads/{new_branch_name}",
        "sha": default_branch_commit_sha
    }

    response = requests.post(new_branch_ref_url, headers=get_github_auth_header(), json=new_branch_ref_data)

    if response.status_code != 201:
        raise Exception(f"Failed to create new branch '{new_branch_name}': {response.status_code} - {response.text}")

    print(f"Created new branch '{new_branch_name}' in repository '{repo_full_name}'")

def get_github_auth_header():
    return {"Authorization": f"token {GITHUB_API_KEY}"}

def apply_modifications(repo_data, branch_name, modifications):
    repo_full_name = repo_data["full_name"]

    # Concatenate modifications into a single string
    modifications_text = "Modifications:\n"
    for modification in modifications:
        modifications_text += f"{modification}\n"

    # Convert the modifications text to base64 encoding
    content_base64 = base64.b64encode(modifications_text.encode()).decode()

    # Send a request to the GitHub API to create the file in the repository
    create_file_url = f"https://api.github.com/repos/{repo_full_name}/contents/{branch_name}"
    create_file_data = {
        "message": f"Create file '{branch_name}' with modifications",
        "content": content_base64,
        "branch": branch_name
    }

    # print the url and data
    print(f"{branch_name}\n---\n{create_file_url}")

    response = requests.put(create_file_url, headers=get_github_auth_header(), json=create_file_data)

    if response.status_code != 201:
        raise Exception(f"Failed to create file '{branch_name}' in repository '{repo_full_name}': {response.status_code} - {response.text}")

    print(f"Created file '{branch_name}' in repository '{repo_full_name}' with modifications")


def create_pull_request(repo_data, branch_name, issue_data):
    # TODO: Implement creating a pull request comparing the new branch with the default branch
    pass
