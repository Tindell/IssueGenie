import os
import requests

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
    # TODO: Implement applying modifications to the corresponding files in the new branch
    pass

def create_pull_request(repo_data, branch_name, issue_data):
    # TODO: Implement creating a pull request comparing the new branch with the default branch
    pass
