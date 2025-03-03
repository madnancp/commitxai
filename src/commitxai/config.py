from dataclasses import dataclass
from pathlib import Path


@dataclass
class Constants:
    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    ARTIFACTS_DIR: Path = PROJECT_DIR / "artifacts"
    DATA_DIR: Path = ARTIFACTS_DIR / "data"
