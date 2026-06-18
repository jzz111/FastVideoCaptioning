from cli.models import (
    DEFAULT_BLACKLIST_PATH,
    DEFAULT_MODEL,
    DEFAULT_VOCABULARY_PATH,
    CaptionGenerationRequest,
    CliResult,
    ParsedArgs,
)
from cli.ports import CaptionWorkflow


def run_caption_generation(parsed: ParsedArgs, caption_workflow: CaptionWorkflow | None) -> CliResult:
    request = CaptionGenerationRequest(
        input_path=parsed.input_path or "",
        markers_path=parsed.markers_path or "",
        output_path=parsed.output_path or "",
        model=parsed.model or DEFAULT_MODEL,
        vocabulary_path=parsed.vocabulary_path or DEFAULT_VOCABULARY_PATH,
        blacklist_path=parsed.blacklist_path or DEFAULT_BLACKLIST_PATH,
    )

    if caption_workflow is None:
        return CliResult(
            exit_code=1,
            stderr="Caption-generation workflow is not configured.",
        )

    caption_workflow(request)
    return CliResult(
        exit_code=0,
        stdout=f"Caption-generation workflow started for {request.input_path}.\n",
    )
