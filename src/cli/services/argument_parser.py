from collections.abc import Sequence

from cli.models import ParsedArgs


def parse_cli_args(args: Sequence[str]) -> ParsedArgs:
    if "--help" in args or "-h" in args:
        return ParsedArgs(help_requested=True)

    if not args:
        return ParsedArgs(error="No command line arguments were provided. Use --help for usage information.")

    values: dict[str, str | bool] = {}
    options_requiring_values = {
        "--input",
        "--markers",
        "--output",
        "--model",
        "--vocabulary",
        "--blacklist",
        "--download-model",
    }
    flags = {"--manage-models"}

    index = 0
    while index < len(args):
        token = args[index]
        if token in flags:
            values[token] = True
            index += 1
            continue

        if token in options_requiring_values:
            if index + 1 >= len(args) or args[index + 1].startswith("-"):
                return ParsedArgs(error=f"{token} requires a value.")
            values[token] = args[index + 1]
            index += 2
            continue

        return ParsedArgs(error=f"Unsupported argument: {token}")

    return ParsedArgs(
        manage_models=bool(values.get("--manage-models")),
        input_path=_string_value(values.get("--input")),
        markers_path=_string_value(values.get("--markers")),
        output_path=_string_value(values.get("--output")),
        model=_string_value(values.get("--model")),
        vocabulary_path=_string_value(values.get("--vocabulary")),
        blacklist_path=_string_value(values.get("--blacklist")),
        download_model=_string_value(values.get("--download-model")),
    )


def _string_value(value: str | bool | None) -> str | None:
    return value if isinstance(value, str) else None
