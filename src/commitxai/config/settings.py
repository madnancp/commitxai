from pathlib import Path
from dataclasses import dataclass
from platformdirs import user_cache_dir


@dataclass
class Settings:
    APP_NAME: str = "commitxai"
    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    DATA_DIR: Path = ARTIFACTS_DIR / "data"

    CACHE_DIR: str = user_cache_dir(appname=APP_NAME, appauthor=False)
