from cli.models import ALTERNATE_MODEL, DEFAULT_MODEL, CliResult, ParsedArgs
from cli.ports import ModelManager


def run_model_management(parsed: ParsedArgs, model_manager: ModelManager | None) -> CliResult:
    if model_manager is None:
        return CliResult(exit_code=1, stderr="Model-management workflow is not configured.")

    if parsed.download_model:
        model_manager.download_model(parsed.download_model)

    downloaded_models = list(model_manager.list_downloaded_models())
    lines = [
        "Model management",
        "",
        "Available transcription models:",
        f"- {DEFAULT_MODEL} (OpenAI Whisper Large-v3, default)",
        f"- {ALTERNATE_MODEL} (OpenAI Distil-Whisper, alternate)",
        "",
        "Locally downloaded transcription models:",
    ]

    if downloaded_models:
        lines.extend(f"- {model}" for model in downloaded_models)
    else:
        lines.append("- None")

    if parsed.download_model:
        lines.extend(["", f"Download requested for {parsed.download_model}."])

    return CliResult(exit_code=0, stdout="\n".join(lines) + "\n")
