from pathlib import Path
from dataclasses import dataclass


@dataclass
class Settings:
    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    DATA_DIR: Path = ARTIFACTS_DIR / "data"
