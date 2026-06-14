# ADR 0003: Use Pragmatic Hexagonal Architecture for the MVP

## Status

Accepted

## Date

2026-06-14

## Requirement References

- `0.1` - Command Line Arguments
- `1.1` - Manage Transcription Models
- `1.2` - Transcript Generation
- `2.1` - Vocabulary Correction
- `2.2` - Caption Cleanup
- `2.3` - Caption Export

## Context

Fast Video Captioning is a personal project, but it still needs a clear architecture that keeps the captioning workflow readable, testable, and maintainable.

The product has several external concerns:

- Command line input.
- Local media files.
- Model downloads.
- Whisper transcription implementations.
- Vocabulary and correction-memory files.
- Caption and review output files.

The core product behavior should not become tightly coupled to those external details. The project owner is familiar with .NET-style solution boundaries such as startup, application, domain, data, and interface-specific projects. Hexagonal architecture maps well to that mental model while providing precise language for boundaries.

## Decision

The MVP will use a pragmatic hexagonal architecture style.

The project will use the following vocabulary:

- `application` for workflow orchestration and use cases.
- `domain` for product concepts, value objects, and validation.
- `ports` for interfaces or protocols the application core depends on.
- `adapters` for concrete implementations that connect ports to files, models, command line input, or other external systems.
- `cli` for the startup and entry point.

In .NET solution terms:

- `cli` maps to the startup or entry-point project.
- `application` maps to core application logic.
- `domain` maps to domain objects and product rules.
- `ports` map to C#-style interfaces such as `ITranscriber` or `ICaptionWriter`.
- `adapters` map to concrete integration projects such as data access, Whisper integration, filesystem output, or CLI parsing.

The MVP should use this architecture lightly. Constructor injection, function parameters, Python protocols, and focused modules are preferred over a dependency injection container or heavy framework structure.

## Consequences

The project gets a shared vocabulary for boundaries before implementation starts.

Core workflow code should remain testable without downloading models, reading real media, or writing production output files.

Adapters can change independently as the product evolves from CLI-only usage toward possible future interfaces.

The architecture introduces some structure early, so implementation should avoid unnecessary ceremony. If a boundary or abstraction does not improve readability, testability, or changeability, it should wait.
