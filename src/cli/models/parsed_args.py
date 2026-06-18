from dataclasses import dataclass


@dataclass(frozen=True)
class ParsedArgs:
    help_requested: bool = False
    manage_models: bool = False
    input_path: str | None = None
    markers_path: str | None = None
    output_path: str | None = None
    model: str | None = None
    vocabulary_path: str | None = None
    blacklist_path: str | None = None
    download_model: str | None = None
    error: str | None = None
