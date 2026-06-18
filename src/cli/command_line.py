from __future__ import annotations

from typing import Sequence

from cli.models import (
    ALTERNATE_MODEL,
    DEFAULT_BLACKLIST_PATH,
    DEFAULT_MODEL,
    DEFAULT_VOCABULARY_PATH,
    CaptionGenerationRequest,
    CliResult,
)
from cli.ports import CaptionWorkflow, ModelManager
from cli.services.argument_parser import parse_cli_args
from cli.services.argument_validator import validate_cli_args
from cli.services.caption_generation_runner import run_caption_generation
from cli.services.help_text_builder import build_help_text
from cli.services.model_management_runner import run_model_management


def run_cli(
    args: Sequence[str],
    caption_workflow: CaptionWorkflow | None = None,
    model_manager: ModelManager | None = None,
) -> CliResult:
    parsed = parse_cli_args(args)

    if parsed.help_requested:
        return CliResult(exit_code=0, stdout=build_help_text())

    if parsed.error:
        return CliResult(exit_code=2, stderr=parsed.error)

    validation_error = validate_cli_args(parsed)
    if validation_error:
        return CliResult(exit_code=2, stderr=validation_error)

    if parsed.manage_models:
        return run_model_management(parsed, model_manager)

    return run_caption_generation(parsed, caption_workflow)
