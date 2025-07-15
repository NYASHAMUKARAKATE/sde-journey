import requests
from rich import print
from rich.table import Table
import os

GITHUB_API = "https://api.github.com"
USERNAME = os.getenv("GITHUB_USERNAME", "username ") 

def github_dashboard():
    user_url = f"{GITHUB_API}/users/{USERNAME}"
    repos_url = f"{GITHUB_API}/users/{USERNAME}/repos"

    try:
        user_resp = requests.get(user_url)
        repos_resp = requests.get(repos_url)
        user_data = user_resp.json()
        repos_data = repos_resp.json()

        print(f"\n[bold cyan]GitHub Profile for [@{USERNAME}][/bold cyan]")
        print(f"Name: {user_data.get('name')} | Public Repos: {user_data.get('public_repos')} | Followers: {user_data.get('followers')}")

        table = Table(title="Repositories")
        table.add_column("Name", style="magenta")
        table.add_column("Stars", justify="right")
        table.add_column("Forks", justify="right")

        for repo in repos_data[:10]: 
            table.add_row(repo['name'], str(repo['stargazers_count']), str(repo['forks_count']))

        print(table)

    except Exception as e:
        print(f"[red]Failed to fetch GitHub data:[/red] {e}")
