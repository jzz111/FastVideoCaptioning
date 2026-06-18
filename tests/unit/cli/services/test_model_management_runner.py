import unittest

from cli.models import ALTERNATE_MODEL, DEFAULT_MODEL, ParsedArgs
from cli.services.model_management_runner import run_model_management


class RecordingModelManager:
    def __init__(self, downloaded_models=None):
        self.downloaded_models = downloaded_models or []
        self.download_requests = []

    def list_downloaded_models(self):
        return self.downloaded_models

    def download_model(self, model_name):
        self.download_requests.append(model_name)


class ModelManagementRunnerTests(unittest.TestCase):
    def test_missing_model_manager_returns_configuration_error(self):
        result = run_model_management(ParsedArgs(manage_models=True), model_manager=None)

        self.assertNotEqual(0, result.exit_code)
        self.assertIn("Model-management workflow is not configured", result.stderr)

    def test_displays_available_and_downloaded_models(self):
        manager = RecordingModelManager(downloaded_models=[ALTERNATE_MODEL])

        result = run_model_management(ParsedArgs(manage_models=True), manager)

        self.assertEqual(0, result.exit_code)
        self.assertIn(DEFAULT_MODEL, result.stdout)
        self.assertIn(ALTERNATE_MODEL, result.stdout)
        self.assertIn("OpenAI Whisper Large-v3", result.stdout)
        self.assertIn("OpenAI Distil-Whisper", result.stdout)
        self.assertIn("Locally downloaded transcription models", result.stdout)

    def test_displays_none_when_no_models_are_downloaded(self):
        manager = RecordingModelManager()

        result = run_model_management(ParsedArgs(manage_models=True), manager)

        self.assertIn("- None", result.stdout)

    def test_requests_model_download_when_selected(self):
        manager = RecordingModelManager()

        result = run_model_management(ParsedArgs(manage_models=True, download_model=ALTERNATE_MODEL), manager)

        self.assertEqual([ALTERNATE_MODEL], manager.download_requests)
        self.assertIn(f"Download requested for {ALTERNATE_MODEL}", result.stdout)


if __name__ == "__main__":
    unittest.main()
