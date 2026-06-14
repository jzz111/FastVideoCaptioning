# ADR 0001: Use Whisper Large-v3 as the Default Captioning Model

## Status

Accepted

## Date

2026-06-05

## Requirement References

- `1.1` - Manage Transcription Models
- `1.2` - Transcript Generation

## Context

Fast Video Captioning needs to generate accurate captions from source video or audio files. The MVP requirements include model management, local model downloads, and transcript generation using a selected transcription model.

The project currently recognizes two model options:

- OpenAI Whisper Large-v3 as the default captioning model.
- OpenAI Distil-Whisper as an alternate captioning model.

The default should be explicit because transcription quality is central to the product. Alternate models should remain configurable because users may need different tradeoffs for speed, resource usage, or local availability.

## Decision

Fast Video Captioning will use OpenAI Whisper Large-v3 as the default captioning model.

OpenAI Distil-Whisper will be supported as an alternate configurable model.

Model selection and model download behavior must be deterministic and testable:

- The default model must be visible in configuration and user-facing model management output.
- Alternate models must be selected explicitly.
- Downloaded models must be stored in `local/models`.
- Missing, unavailable, or failed model downloads must produce clear errors.
- The application must not silently switch models when the requested model is unavailable.

## Consequences

Whisper Large-v3 becomes the baseline for caption quality and expected output behavior.

The application needs a clear model registry or configuration source that identifies the default model and available alternate models.

Tests should verify default model selection, explicit alternate selection, local model detection, download location, and failure handling.

Future model additions should extend the configurable model list without changing the default unless a new ADR supersedes this decision.
