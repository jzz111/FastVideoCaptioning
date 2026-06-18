import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from cli.command_line import (  # noqa: E402
    DEFAULT_BLACKLIST_PATH,
    DEFAULT_MODEL,
    DEFAULT_VOCABULARY_PATH,
    ALTERNATE_MODEL,
    CaptionGenerationRequest,
    run_cli,
)


class RecordingModelManager:
    def __init__(self, downloaded_models=None):
        self.downloaded_models = downloaded_models or []
        self.download_requests = []

    def list_downloaded_models(self):
        return self.downloaded_models

    def download_model(self, model_name):
        self.download_requests.append(model_name)


class CliHelpContractTests(unittest.TestCase):
    def test_help_flag_exits_successfully_and_lists_epic_0_contract(self):
        for help_flag in ("--help", "-h"):
            with self.subTest(help_flag=help_flag):
                result = run_cli([help_flag])

                self.assertEqual(0, result.exit_code)
                self.assertEqual("", result.stderr)
                self.assertIn("--input", result.stdout)
                self.assertIn("--markers", result.stdout)
                self.assertIn("--output", result.stdout)
                self.assertIn("--model", result.stdout)
                self.assertIn("--vocabulary", result.stdout)
                self.assertIn("--blacklist", result.stdout)
                self.assertIn("--manage-models", result.stdout)
                self.assertIn("--download-model", result.stdout)
                self.assertIn("caption --input video.mp4 --markers markers.txt --output captions.txt", result.stdout)
                self.assertIn("caption --manage-models --download-model distil-whisper", result.stdout)
                self.assertIn(DEFAULT_VOCABULARY_PATH, result.stdout)
                self.assertIn(DEFAULT_BLACKLIST_PATH, result.stdout)
                self.assertIn("OpenAI Whisper Large-v3", result.stdout)
                self.assertIn("OpenAI Distil-Whisper", result.stdout)
                self.assertIn("Marker export file for YouTube timeline chapters", result.stdout)


class CliValidationContractTests(unittest.TestCase):
    def test_caption_generation_requires_input_markers_and_output(self):
        cases = [
            (["--markers", "markers.txt", "--output", "captions.txt"], "--input"),
            (["--input", "video.mp4", "--output", "captions.txt"], "--markers"),
            (["--input", "video.mp4", "--markers", "markers.txt"], "--output"),
        ]

        for args, missing_argument in cases:
            with self.subTest(missing_argument=missing_argument):
                workflow_calls = []

                result = run_cli(args, caption_workflow=workflow_calls.append)

                self.assertNotEqual(0, result.exit_code)
                self.assertIn("Missing required argument", result.stderr)
                self.assertIn(missing_argument, result.stderr)
                self.assertEqual([], workflow_calls)

    def test_manage_models_is_allowed_without_caption_generation_arguments(self):
        manager = RecordingModelManager(downloaded_models=[DEFAULT_MODEL])

        result = run_cli(["--manage-models"], model_manager=manager)

        self.assertEqual(0, result.exit_code)
        self.assertIn("Available transcription models", result.stdout)
        self.assertIn("Locally downloaded transcription models", result.stdout)
        self.assertIn(DEFAULT_MODEL, result.stdout)

    def test_invalid_argument_combinations_are_rejected_before_processing(self):
        workflow_calls = []
        manager = RecordingModelManager()

        result = run_cli(
            ["--manage-models", "--input", "video.mp4"],
            caption_workflow=workflow_calls.append,
            model_manager=manager,
        )

        self.assertNotEqual(0, result.exit_code)
        self.assertIn("--manage-models cannot be combined", result.stderr)
        self.assertEqual([], workflow_calls)
        self.assertEqual([], manager.download_requests)

    def test_download_model_requires_model_management_mode(self):
        result = run_cli(["--download-model", DEFAULT_MODEL])

        self.assertNotEqual(0, result.exit_code)
        self.assertIn("--download-model requires --manage-models", result.stderr)

    def test_unsupported_models_are_rejected(self):
        result = run_cli(
            [
                "--input",
                "video.mp4",
                "--markers",
                "markers.txt",
                "--output",
                "captions.txt",
                "--model",
                "unknown-model",
            ]
        )

        self.assertNotEqual(0, result.exit_code)
        self.assertIn("Unsupported model", result.stderr)


class CaptionGenerationDispatchContractTests(unittest.TestCase):
    def test_valid_caption_arguments_start_caption_generation_workflow(self):
        workflow_calls = []

        result = run_cli(
            [
                "--input",
                "video.mp4",
                "--markers",
                "markers.txt",
                "--output",
                "captions.txt",
                "--model",
                ALTERNATE_MODEL,
                "--vocabulary",
                "channel-vocabulary.csv",
                "--blacklist",
                "blacklist.csv",
            ],
            caption_workflow=workflow_calls.append,
        )

        self.assertEqual(0, result.exit_code)
        self.assertEqual(1, len(workflow_calls))
        self.assertEqual(
            CaptionGenerationRequest(
                input_path="video.mp4",
                markers_path="markers.txt",
                output_path="captions.txt",
                model=ALTERNATE_MODEL,
                vocabulary_path="channel-vocabulary.csv",
                blacklist_path="blacklist.csv",
            ),
            workflow_calls[0],
        )

    def test_caption_generation_uses_default_optional_values(self):
        workflow_calls = []

        result = run_cli(
            ["--input", "video.mp4", "--markers", "markers.txt", "--output", "captions.txt"],
            caption_workflow=workflow_calls.append,
        )

        self.assertEqual(0, result.exit_code)
        self.assertEqual(1, len(workflow_calls))
        self.assertEqual(DEFAULT_MODEL, workflow_calls[0].model)
        self.assertEqual(DEFAULT_VOCABULARY_PATH, workflow_calls[0].vocabulary_path)
        self.assertEqual(DEFAULT_BLACKLIST_PATH, workflow_calls[0].blacklist_path)

    def test_successful_validation_requires_configured_caption_workflow(self):
        result = run_cli(["--input", "video.mp4", "--markers", "markers.txt", "--output", "captions.txt"])

        self.assertNotEqual(0, result.exit_code)
        self.assertIn("Caption-generation workflow is not configured", result.stderr)


class ModelManagementDispatchContractTests(unittest.TestCase):
    def test_manage_models_displays_available_and_downloaded_models(self):
        manager = RecordingModelManager(downloaded_models=[ALTERNATE_MODEL])

        result = run_cli(["--manage-models"], model_manager=manager)

        self.assertEqual(0, result.exit_code)
        self.assertIn(DEFAULT_MODEL, result.stdout)
        self.assertIn(ALTERNATE_MODEL, result.stdout)
        self.assertIn("OpenAI Whisper Large-v3", result.stdout)
        self.assertIn("OpenAI Distil-Whisper", result.stdout)
        self.assertIn("Locally downloaded transcription models", result.stdout)

    def test_manage_models_allows_model_selection_for_download(self):
        manager = RecordingModelManager()

        result = run_cli(["--manage-models", "--download-model", ALTERNATE_MODEL], model_manager=manager)

        self.assertEqual(0, result.exit_code)
        self.assertEqual([ALTERNATE_MODEL], manager.download_requests)
        self.assertIn(f"Download requested for {ALTERNATE_MODEL}", result.stdout)

    def test_manage_models_prevents_caption_generation_processing(self):
        workflow_calls = []
        manager = RecordingModelManager()

        result = run_cli(
            ["--manage-models"],
            caption_workflow=workflow_calls.append,
            model_manager=manager,
        )

        self.assertEqual(0, result.exit_code)
        self.assertEqual([], workflow_calls)

    def test_successful_model_management_requires_configured_model_manager(self):
        result = run_cli(["--manage-models"])

        self.assertNotEqual(0, result.exit_code)
        self.assertIn("Model-management workflow is not configured", result.stderr)


if __name__ == "__main__":
    unittest.main()
