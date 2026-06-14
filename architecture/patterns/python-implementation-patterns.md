# Python Implementation Patterns

Fast Video Captioning should use Python patterns that support readable, testable code without importing unnecessary framework habits.

## Modules and Boundaries

Prefer modules that match product responsibilities.

Possible future source layout:

```text
src/
`-- fast_video_captioning/
    |-- domain/
    |-- application/
    |-- ports/
    |-- adapters/
    `-- cli/
```

This layout is a direction, not a requirement. Introduce it when implementation work needs it.

## Protocols and Abstract Base Classes

Use Python `Protocol` types or abstract base classes when a boundary needs to be testable or replaceable.

Prefer `Protocol` for simple structural contracts:

```python
class Transcriber(Protocol):
    def transcribe(self, clip: MediaClip, model: TranscriptionModel) -> Transcript:
        ...
```

Avoid defining interfaces for every class. A protocol should exist because the application has more than one implementation, needs a test double, or must protect the core workflow from an external dependency.

## Dataclasses

Use dataclasses for simple domain values that are mostly data with validation or clear meaning.

Good candidates include:

- `MediaClip`
- `TranscriptionModel`
- `Transcript`
- `CaptionDocument`
- `VocabularyCorrection`

Keep dataclasses focused. If behavior grows large, move orchestration into an application service or workflow object.

## Dependency Injection

Prefer explicit dependency injection through constructors or function arguments.

Avoid global service locators and hidden module-level dependencies for workflow behavior. They make tests harder and make it less clear which files, models, or stores are being used.

## SOLID, Practically

Use SOLID as judgment, not as a checklist.

- Keep classes and functions focused on one reason to change.
- Depend on ports or protocols when external systems are involved.
- Keep contracts small and specific.
- Make behavior replaceable where tests or product requirements need replacement.

Do not split code into tiny classes just to satisfy a principle by name.

## DRY, Practically

Avoid duplication that creates maintenance risk.

Allow small duplication when it keeps early code readable. Extract shared code once repetition has a clear shape and a shared abstraction would be easier to understand than the duplicate code.

## Error Handling

Errors should be clear and actionable.

Handle missing files, invalid timestamps, unavailable models, failed downloads, invalid vocabulary files, and output write failures with messages that explain what went wrong and what input or path caused it.

Do not silently fall back to another model, skip output, or discard correction memory.

## Tests

Use tests to protect workflow behavior and architecture boundaries.

Prefer fake adapters or temporary files over real model downloads in unit tests. Model download behavior should be deterministic and testable without requiring network access unless the test is explicitly an integration test.
