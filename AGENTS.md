# AI Context

## Project

Fast Video Captioning is a caption-generation project for content creators. The product should turn source video or audio into clean captions that can be reviewed, corrected, and reused for future captioning improvements.

## Core Inputs

The system should support:

- A video or audio file.
- Clip start and end timestamps.
- Optional channel-specific vocabulary for names, phrases, jargon, or recurring terms.

## Core Outputs

The system should produce:

- Clean `.txt` captions.
- A human review file for checking and correcting generated captions.
- Correction memory that can improve future captioning runs.

## Captioning Models

The finished product must be able to download captioning models required for transcription and caption generation.

Current model options:

- OpenAI Whisper Large-v3 is the default captioning model.
- OpenAI Distil-Whisper is the alternate captioning model.

When implementing model selection or downloads, keep the default explicit and make alternate models configurable.

## Product Behavior

Preserve human review as a first-class part of the workflow. Generated captions should be auditable and easy to correct.

Correction memory should be treated as project data that helps future runs, not as an opaque side effect.

Caption output should favor clarity and usability for content creators over clever formatting.

## Implementation Guidance

Before changing code:

- Read the README and relevant source files.
- Keep changes scoped to the requested behavior.
- Prefer existing project patterns once they exist.
- Avoid unrelated refactors.

During implementation:

- Make model download behavior deterministic and testable.
- Keep file paths, generated outputs, and model configuration explicit.
- Handle missing files, invalid timestamps, unavailable models, and failed downloads with clear errors.
- Do not silently discard generated captions, review data, or correction memory.

Before finishing:

- Run relevant tests or verification scripts.
- Report what changed and what was verified.
- State any verification that could not be run.

