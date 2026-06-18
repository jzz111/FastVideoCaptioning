import unittest

from cli.models import ALTERNATE_MODEL, DEFAULT_MODEL, ParsedArgs
from cli.services.argument_validator import validate_cli_args


class ArgumentValidatorTests(unittest.TestCase):
    def test_valid_caption_generation_arguments_have_no_error(self):
        error = validate_cli_args(
            ParsedArgs(
                input_path="video.mp4",
                markers_path="markers.txt",
                output_path="captions.txt",
                model=DEFAULT_MODEL,
            )
        )

        self.assertIsNone(error)

    def test_caption_generation_requires_input_markers_and_output(self):
        error = validate_cli_args(ParsedArgs())

        self.assertIn("--input", error)
        self.assertIn("--markers", error)
        self.assertIn("--output", error)

    def test_manage_models_allows_no_caption_generation_arguments(self):
        error = validate_cli_args(ParsedArgs(manage_models=True))

        self.assertIsNone(error)

    def test_manage_models_rejects_caption_generation_arguments(self):
        error = validate_cli_args(ParsedArgs(manage_models=True, input_path="video.mp4", model=DEFAULT_MODEL))

        self.assertIn("--manage-models cannot be combined", error)
        self.assertIn("--input", error)
        self.assertIn("--model", error)

    def test_download_model_requires_manage_models(self):
        error = validate_cli_args(ParsedArgs(download_model=DEFAULT_MODEL))

        self.assertEqual("--download-model requires --manage-models.", error)

    def test_unsupported_caption_model_is_rejected(self):
        error = validate_cli_args(
            ParsedArgs(
                input_path="video.mp4",
                markers_path="markers.txt",
                output_path="captions.txt",
                model="unknown-model",
            )
        )

        self.assertIn("Unsupported model 'unknown-model'", error)

    def test_supported_download_model_is_allowed_in_model_management(self):
        error = validate_cli_args(ParsedArgs(manage_models=True, download_model=ALTERNATE_MODEL))

        self.assertIsNone(error)


if __name__ == "__main__":
    unittest.main()
