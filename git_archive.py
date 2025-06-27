import requests

def archive_github_repo(user, repo_name, git_token):
    """
    Archive a GitHub repository (make it read-only)
    """
    url = f"https://github.com/{user}/{repo_name}"

    headers = {
        'Authorization': f'token {git_token}'
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

archive_github_repo(user, repo_name, git_token)
