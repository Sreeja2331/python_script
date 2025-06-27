import requests
import sys

def archive_github_repo(repo_name, git_token):
    """
    Archive a GitHub repository (make it read-only)
    """
    url = f"https://github.com/Sreeja2331/{repo_name}"

    headers = {
        'Authorization': f'token {git_token}'
        'Accept: application/vnd.github.v3+json'
    }

    data = {
        'archived': True  
    }

    response = requests.patch(url, json=data, headers=headers)

    if response.status_code == 200:
        print(f"Repository '{repo_name}' has been archived successfully!")
    else:
        print(f"Failed to archive the repository. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    repo_name = sys.argv[1]
    git_token = sys.argv[2]

    archive_github_repo(repo_name, git_token)
