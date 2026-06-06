# Epic 1: Media Processing


## Feature 1: Manage Transcription Models

### Story 1: Display model status
#### Description
When the user choses to enter Model Management mode, the user will be given a list of all models that are available to use with `[local] ` next to any entry that is already downloaded.

#### Acceptance Criteria
- Detect existing local model
- Detect available models

### Story 2: Download selected Whisper model
#### Description
In the model status screen, if the user selects a model that is not downloaded and without the designation of `[local/models]` next to it on the list, the application will prompt the user "Would you like to download this model?" with the choice of "[Y]n" where Y is the default for downloading the model locally. The application will save the downloaded model to the local directory of `local`.

#### Acceptance Criteria

- User can select an available model
- User is prompted before download begins
- Downloaded model is stored in local/models
- Download progress is displayed
- User is notified when download completes
- User is notified when download fails


## Feature 2: Transcript Generation

### Story 1: Generate transcript from media file
#### Description
When the user choses to not go into the model management mode, the user will designate the input video file. If the file exists and is of a supported format, the application will generate a transcript using the selected transcription model and save the output to the specified location.

#### Acceptance Criteria

- User must provide an input filename that exists
- Supported formats are validated
- Unsupported formats are rejected with a user-friendly message
- User can select a transcription model
- Transcript is generated using the selected model
- Transcript generation progress is displayed
- Transcript output is saved
- User is notified when transcription fails