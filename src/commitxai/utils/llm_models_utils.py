import os
from huggingface_hub import hf_hub_download
from commitxai.config.settings import Settings


MODELS = {
    "TheBloke/phi-2-GGUF": "phi-2.Q8_0.gguf",
    "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF": "tinyllama-1.1b-chat-v1.0.Q8_0.gguf",
}


def download_n_store_model_on_cache(model: str) -> None:
    try:
        os.makedirs(name=f"{Settings.CACHE_DIR}/models/", exist_ok=True)
        hf_hub_download(
            repo_id=model,
            filename=MODELS[model],
            cache_dir=f"{Settings.CACHE_DIR}/models",
        )
    except Exception as e:
        print("Something happened in download model as : ", e)
