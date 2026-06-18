from cli.models import ALTERNATE_MODEL, DEFAULT_BLACKLIST_PATH, DEFAULT_MODEL, DEFAULT_VOCABULARY_PATH


def build_help_text() -> str:
    return f"""Fast Video Captioning

Usage:
  caption --input VIDEO_OR_AUDIO --markers MARKERS --output CAPTIONS [options]
  caption --manage-models [--download-model MODEL]
  caption --help

Caption-generation arguments:
  --input PATH          Source video or audio file.
  --markers PATH        Marker export file for YouTube timeline chapters.
  --output PATH         Clean caption .txt output path.
  --model MODEL         Transcription model. Defaults to {DEFAULT_MODEL}.
  --vocabulary PATH     Channel vocabulary correction file. Defaults to {DEFAULT_VOCABULARY_PATH}.
  --blacklist PATH      Blacklist vocabulary file. Defaults to {DEFAULT_BLACKLIST_PATH}.

Model-management arguments:
  --manage-models       Display and manage transcription models.
  --download-model MODEL
                        Download a supported transcription model.

Supported transcription models:
  {DEFAULT_MODEL}       OpenAI Whisper Large-v3. Default captioning model.
  {ALTERNATE_MODEL}     OpenAI Distil-Whisper. Alternate captioning model.

Examples:
  caption --input video.mp4 --markers markers.txt --output captions.txt
  caption --manage-models --download-model {ALTERNATE_MODEL}
"""
