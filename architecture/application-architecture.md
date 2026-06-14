# Application Architecture

Fast Video Captioning should use a pragmatic hexagonal architecture style.

This means the core captioning workflow should be separated from infrastructure concerns such as command line parsing, local files, model downloads, and Whisper-specific transcription code.

## Architectural Intent

The application core should describe the product workflow:

1. Accept media input and clip boundaries.
2. Select or resolve the transcription model.
3. Generate a transcript.
4. Apply vocabulary and correction memory.
5. Produce clean captions.
6. Produce review artifacts.
7. Preserve correction memory for future runs.

The core workflow should not need to know whether it is called from a CLI, test, future web UI, or batch process.

## Hexagonal Shape

Use ports to describe what the workflow needs from the outside world.

Likely ports include:

- `Transcriber`
- `ModelRepository`
- `MediaClipReader`
- `VocabularyStore`
- `CorrectionMemoryStore`
- `CaptionWriter`
- `ReviewArtifactWriter`

Use adapters to connect those ports to real tools and files.

Likely adapters include:

- CLI argument parsing.
- Local filesystem reads and writes.
- Whisper Large-v3 transcription.
- Distil-Whisper transcription.
- CSV vocabulary files.
- Text caption output.
- Review file output.

## Translation from .NET Solution Language

The project will use hexagonal architecture vocabulary, but it maps closely to common .NET solution boundaries.

| Hexagonal term | .NET-style equivalent | Purpose in this project |
| --- | --- | --- |
| `cli` | Startup or entry-point project | Parses command line input, wires dependencies, and starts the workflow. |
| `application` | Core application logic | Orchestrates use cases such as generating captions for a media clip. |
| `domain` | Domain objects project | Holds product concepts, value objects, validation, and product rules. |
| `ports` | Interface project or shared contracts | Defines what the application needs, such as transcribing, writing captions, or storing correction memory. |
| `adapters` | Data, integration, or implementation projects | Implements ports using Whisper, local files, CSV, text output, or other external systems. |

In short: a port is the interface the application depends on, and an adapter is the concrete implementation plugged into that interface.

## Dependency Direction

Dependencies should point inward.

Application workflow code may depend on domain concepts and ports. Adapters may depend on external libraries, filesystems, model APIs, and command line details.

The application core should not import adapter-specific implementation details unless there is a deliberate reason.

## Domain-Driven Naming

Use domain-driven design as a naming and modeling discipline.

This project does not need heavy enterprise DDD ceremony. It does benefit from using the product's real nouns and workflow boundaries in the code.

Prefer explicit domain objects for concepts that carry behavior or validation, such as:

- Media file path and clip timestamps.
- Selected transcription model.
- Transcript text.
- Caption output.
- Review artifact.
- Correction memory.

Avoid making every data shape a class before behavior or validation exists.

## Dependency Injection

Use simple dependency injection.

In Python, constructor arguments and function parameters are usually enough. A dependency injection container is not needed for the MVP unless the application becomes complex enough to justify one.

The goal is testability and clear wiring:

```python
workflow = CaptioningWorkflow(
    transcriber=whisper_transcriber,
    correction_memory=csv_correction_memory,
    caption_writer=text_caption_writer,
)
```

Tests should be able to pass fake or in-memory implementations of ports without downloading models, reading real media, or writing production output files.

## When to Add Abstractions

Add an abstraction when it makes testing, replacement, or readability better.

Do not add an abstraction only because a future feature might need it. Prefer concrete code until a second implementation, test boundary, or meaningful change pressure appears.
