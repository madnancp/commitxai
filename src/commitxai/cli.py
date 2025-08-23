import click
from commitxai.utils import _check_git, download_n_store_model_on_cache


@click.command()
@click.option("--generate", is_flag=True, help="Generate Random Message")
def main(generate: bool):

    if not _check_git():
        return

    if generate:
        try:
            handle_model_selecting()
        except Exception as e:
            click.echo(click.style("Something went wrong.", fg="red"))
    else:
        click.echo("Use --generate to get random joke.!")


def handle_model_selecting() -> None:
    from simple_term_menu import TerminalMenu

    options = ["TheBloke/phi-2-GGUF", "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"]
    menu = TerminalMenu(options, title="Choose which model you want to use")
    selected_idx = menu.show()
    print(f"selected idx : {selected_idx}")
    download_n_store_model_on_cache(options[int(selected_idx)])


if __name__ == "__main__":
    main()
