import click
import requests
from commitxai.utils import is_git_repo, initialize_git


@click.command()
@click.option("--generate", is_flag=True, help="Generate Random Message")
def main(generate: bool):

    if not is_git_repo():
        click.echo("Not a git repository")
        if click.confirm("Do you want to initialize a git repository?"):
            if initialize_git():
                click.echo("Git repository initialized")
            else:
                click.echo("Failed to initialize git repository")
        return

    if generate:
        response = requests.get(
            "https://icanhazdadjoke.com", headers={"Accept": "text/plain"}
        )
        click.echo(response.text)
    else:
        click.echo("Use --generate to get random joke.!")


if __name__ == "__main__":
    main()
