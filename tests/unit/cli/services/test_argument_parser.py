import unittest

from cli.models import ParsedArgs
from cli.services.argument_parser import parse_cli_args


class ArgumentParserTests(unittest.TestCase):
    def test_help_flags_request_help_without_requiring_other_arguments(self):
        for help_flag in ("--help", "-h"):
            with self.subTest(help_flag=help_flag):
                self.assertEqual(ParsedArgs(help_requested=True), parse_cli_args([help_flag]))

    def test_no_arguments_returns_user_facing_parse_error(self):
        parsed = parse_cli_args([])

        self.assertIn("No command line arguments", parsed.error)

    def test_caption_generation_arguments_are_parsed(self):
        parsed = parse_cli_args(
            [
                "--input",
                "video.mp4",
                "--markers",
                "markers.txt",
                "--output",
                "captions.txt",
                "--model",
                "distil-whisper",
                "--vocabulary",
                "vocabulary.csv",
                "--blacklist",
                "blacklist.csv",
            ]
        )

        self.assertEqual("video.mp4", parsed.input_path)
        self.assertEqual("markers.txt", parsed.markers_path)
        self.assertEqual("captions.txt", parsed.output_path)
        self.assertEqual("distil-whisper", parsed.model)
        self.assertEqual("vocabulary.csv", parsed.vocabulary_path)
        self.assertEqual("blacklist.csv", parsed.blacklist_path)

    def test_model_management_arguments_are_parsed(self):
        parsed = parse_cli_args(["--manage-models", "--download-model", "whisper-large-v3"])

        self.assertTrue(parsed.manage_models)
        self.assertEqual("whisper-large-v3", parsed.download_model)

    def test_option_missing_value_returns_parse_error(self):
        parsed = parse_cli_args(["--input"])

        self.assertEqual("--input requires a value.", parsed.error)

    def test_unknown_argument_returns_parse_error(self):
        parsed = parse_cli_args(["--surprise"])

        self.assertEqual("Unsupported argument: --surprise", parsed.error)


if __name__ == "__main__":
    unittest.main()
