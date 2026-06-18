from cli.models import SUPPORTED_MODELS, ParsedArgs


def validate_cli_args(parsed: ParsedArgs) -> str | None:
    if parsed.model and parsed.model not in SUPPORTED_MODELS:
        return _unsupported_model_message(parsed.model)

    if parsed.download_model and parsed.download_model not in SUPPORTED_MODELS:
        return _unsupported_model_message(parsed.download_model)

    if parsed.download_model and not parsed.manage_models:
        return "--download-model requires --manage-models."

    if parsed.manage_models:
        caption_args = {
            "--input": parsed.input_path,
            "--markers": parsed.markers_path,
            "--output": parsed.output_path,
            "--model": parsed.model,
            "--vocabulary": parsed.vocabulary_path,
            "--blacklist": parsed.blacklist_path,
        }
        provided_caption_args = [name for name, value in caption_args.items() if value]
        if provided_caption_args:
            return "--manage-models cannot be combined with caption-generation arguments: " + ", ".join(provided_caption_args)
        return None

    missing = []
    if not parsed.input_path:
        missing.append("--input")
    if not parsed.markers_path:
        missing.append("--markers")
    if not parsed.output_path:
        missing.append("--output")

    if missing:
        return "Missing required argument(s) for caption generation: " + ", ".join(missing)

    return None


def _unsupported_model_message(model: str) -> str:
    return f"Unsupported model '{model}'. Supported models: {', '.join(SUPPORTED_MODELS)}."
