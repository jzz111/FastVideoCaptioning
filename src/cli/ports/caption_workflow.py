from collections.abc import Callable

from cli.models import CaptionGenerationRequest


CaptionWorkflow = Callable[[CaptionGenerationRequest], None]
