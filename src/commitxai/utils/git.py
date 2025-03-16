import subprocess


def _have_staged_changes() -> bool:
    """Check if there are any staged changes in the repository."""
    try:
        subprocess.run(
            ["git", "diff", "--cached", "--quiet"], capture_output=True
        ).check_returncode()
        return False
    except subprocess.CalledProcessError:
        return True


def _is_git_repo() -> bool:
    """Check if the current directory is a git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"], capture_output=True
        ).check_returncode()
        return True
    except subprocess.CalledProcessError:
        return False


def _initialize_git() -> bool:
    """Initialize a git repository in the current directory."""
    try:
        subprocess.run(["git", "init", "-q"]).check_returncode()
        return True
    except subprocess.CalledProcessError:
        return False


def _check_git() -> bool:
    """Check if the current directory is a git repository."""
    import click

    if not _is_git_repo():
        click.echo(click.style("Not a git repository", fg="red"))
        if click.confirm("Do you want to initialize a git repository?"):
            if _initialize_git():
                click.echo(click.style("Git repository initialized", fg="green"))
            else:
                click.echo(click.style("Failed to initialize git repository", fg="red"))
                return False
        else:
            return False

    if not _have_staged_changes():
        click.echo(click.style("No staged changes", fg="red"))
        return False

    return True
