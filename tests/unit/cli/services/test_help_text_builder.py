import unittest

from cli.models import ALTERNATE_MODEL, DEFAULT_BLACKLIST_PATH, DEFAULT_MODEL, DEFAULT_VOCABULARY_PATH
from cli.services.help_text_builder import build_help_text


class HelpTextBuilderTests(unittest.TestCase):
    def test_help_text_describes_supported_workflows_arguments_defaults_and_models(self):
        help_text = build_help_text()

        for expected_text in (
            "--input",
            "--markers",
            "--output",
            "--model",
            "--vocabulary",
            "--blacklist",
            "--manage-models",
            "--download-model",
            "caption --input video.mp4 --markers markers.txt --output captions.txt",
            f"caption --manage-models --download-model {ALTERNATE_MODEL}",
            DEFAULT_MODEL,
            ALTERNATE_MODEL,
            DEFAULT_VOCABULARY_PATH,
            DEFAULT_BLACKLIST_PATH,
            "OpenAI Whisper Large-v3",
            "OpenAI Distil-Whisper",
            "Marker export file for YouTube timeline chapters",
        ):
            with self.subTest(expected_text=expected_text):
                self.assertIn(expected_text, help_text)


if __name__ == "__main__":
    unittest.main()
