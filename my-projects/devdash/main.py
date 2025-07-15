import click
from github.tracker import github_dashboard
from rich.console import Console


@click.group()
def devdash():
    """DevDash CLI for managing development dashboards."""
    pass

@devdash.command()
def github():
    """Show Github profile and its stats """
    github_dashboard()


if __name__ == "__main__":
    devdash()