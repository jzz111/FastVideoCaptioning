# Epic 0: Application Interface

## Feature 1: Command Line Arguments

### Story 1: Display help information

#### Description

When the user runs the application with a help flag, the application will display command line usage information for both supported MVP workflows:

1. Caption generation
2. Model management

The help text will describe all supported command line arguments, default file locations, and provide example usage.

#### Acceptance Criteria

* Display help when the user provides `--help` or `-h`
* List every supported command line argument
* Show a caption-generation workflow example
* Show a model-management workflow example
* Display default file locations for optional files
* Explain supported transcription models
* Explain that `--markers` expects a marker export file for YouTube timeline chapters
* Exit successfully after displaying help

### Story 2: Validate command line arguments

#### Description

The application will validate all command line arguments before starting any processing. Invalid or incomplete argument combinations will be rejected with a user-friendly error message.

#### Acceptance Criteria

* Require `--input` when running the caption-generation workflow
* Require `--markers` when running the caption-generation workflow
* Require `--output` when running the caption-generation workflow
* Allow `--manage-models` without caption-generation arguments
* Reject invalid argument combinations
* Display a user-friendly validation message when required arguments are missing
* Prevent processing when validation fails

### Story 3: Execute caption-generation workflow

#### Description

The application will execute the caption-generation workflow when the required command line arguments are supplied.

#### Acceptance Criteria

* Accept an input media file
* Accept a marker export file
* Accept an output file location
* Accept an optional transcription model selection
* Accept an optional vocabulary correction file location
* Accept an optional blacklist vocabulary file location
* Use default file locations when optional files are not specified
* Start the caption-generation workflow after successful validation

### Story 4: Execute model-management workflow

#### Description

The application will enter model-management mode when the user provides the `--manage-models` argument.

#### Acceptance Criteria

* Open model-management mode when `--manage-models` is provided
* Display available transcription models
* Display locally downloaded transcription models
* Allow selection of a model for download
* Prevent caption-generation processing while model-management mode is active
