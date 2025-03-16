import subprocess


def is_git_repo() -> bool:
    """Check if the current directory is a git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"], capture_output=True
        ).check_returncode()
        return True
    except subprocess.CalledProcessError:
        return False


def initialize_git() -> bool:
    """Initialize a git repository in the current directory."""
    try:
        subprocess.run(["git", "init"]).check_returncode()
        return True
    except subprocess.CalledProcessError:
        return False
