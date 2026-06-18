from dataclasses import dataclass

from .transcription_models import DEFAULT_BLACKLIST_PATH, DEFAULT_MODEL, DEFAULT_VOCABULARY_PATH


@dataclass(frozen=True)
class CaptionGenerationRequest:
    input_path: str
    markers_path: str
    output_path: str
    model: str = DEFAULT_MODEL
    vocabulary_path: str = DEFAULT_VOCABULARY_PATH
    blacklist_path: str = DEFAULT_BLACKLIST_PATH
