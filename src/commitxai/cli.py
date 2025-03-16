import click
import requests
from commitxai.utils import _check_git


@click.command()
@click.option("--generate", is_flag=True, help="Generate Random Message")
def main(generate: bool):

    if not _check_git():
        return

    if generate:
        try:
            response = requests.get(
                "https://icanhazdadjoke.com", headers={"Accept": "text/plain"}
            )
            click.echo(response.text)
        except Exception as e:
            click.echo(click.style("Please Check your network connection.", fg="red"))
    else:
        click.echo("Use --generate to get random joke.!")


if __name__ == "__main__":
    main()
