import unittest

from cli.models import (
    ALTERNATE_MODEL,
    DEFAULT_BLACKLIST_PATH,
    DEFAULT_MODEL,
    DEFAULT_VOCABULARY_PATH,
    CaptionGenerationRequest,
    ParsedArgs,
)
from cli.services.caption_generation_runner import run_caption_generation


class CaptionGenerationRunnerTests(unittest.TestCase):
    def test_missing_caption_workflow_returns_configuration_error(self):
        result = run_caption_generation(
            ParsedArgs(input_path="video.mp4", markers_path="markers.txt", output_path="captions.txt"),
            caption_workflow=None,
        )

        self.assertNotEqual(0, result.exit_code)
        self.assertIn("Caption-generation workflow is not configured", result.stderr)

    def test_calls_caption_workflow_with_requested_values(self):
        workflow_calls = []

        result = run_caption_generation(
            ParsedArgs(
                input_path="video.mp4",
                markers_path="markers.txt",
                output_path="captions.txt",
                model=ALTERNATE_MODEL,
                vocabulary_path="vocabulary.csv",
                blacklist_path="blacklist.csv",
            ),
            caption_workflow=workflow_calls.append,
        )

        self.assertEqual(0, result.exit_code)
        self.assertEqual(
            [
                CaptionGenerationRequest(
                    input_path="video.mp4",
                    markers_path="markers.txt",
                    output_path="captions.txt",
                    model=ALTERNATE_MODEL,
                    vocabulary_path="vocabulary.csv",
                    blacklist_path="blacklist.csv",
                )
            ],
            workflow_calls,
        )

    def test_uses_default_optional_values(self):
        workflow_calls = []

        run_caption_generation(
            ParsedArgs(input_path="video.mp4", markers_path="markers.txt", output_path="captions.txt"),
            caption_workflow=workflow_calls.append,
        )

        self.assertEqual(DEFAULT_MODEL, workflow_calls[0].model)
        self.assertEqual(DEFAULT_VOCABULARY_PATH, workflow_calls[0].vocabulary_path)
        self.assertEqual(DEFAULT_BLACKLIST_PATH, workflow_calls[0].blacklist_path)


if __name__ == "__main__":
    unittest.main()
