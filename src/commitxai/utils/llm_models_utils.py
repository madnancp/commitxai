import os
from enum import Enum
from commitxai.config.settings import Settings


class LlmModels(Enum):
    PHI = 1
    TINYlLAMA = 2
    MISTRAL = 3


def store_model_on_cache() -> None:
    os.makedirs(name=f"{Settings.CACHE_DIR}/models/", exist_ok=True)
    pass


def pull_model_from_hf_hub() -> None:
    pass
