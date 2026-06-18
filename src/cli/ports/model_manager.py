from typing import Protocol, Sequence


class ModelManager(Protocol):
    def list_downloaded_models(self) -> Sequence[str]:
        ...

    def download_model(self, model_name: str) -> None:
        ...
