import click
import requests


@click.command()
@click.option("--generate", is_flag=True, help="Generate Random Message")
def main(generate: bool):
    if generate:
        response = requests.get(
            "https://icanhazdadjoke.com", headers={"Accept": "text/plain"}
        )
        click.echo(response.text)
    else:
        click.echo("Use --generate to get random joke.!")


if __name__ == "__main__":
    main()
