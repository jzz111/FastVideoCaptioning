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

## Requirements Work Items

Requirement work item references use `{epic}.{feature}.{story}`.

Examples:

- `0.1.1` means epic `0`, feature `1`, story `1`.
- `0.1` means epic `0`, feature `1`.

## Implementation Guidance

Before changing code:

- Read the README and relevant source files.
- Read relevant architecture docs when implementation choices involve structure, boundaries, model behavior, generated outputs, review data, or correction memory.
- Read `architecture/tech-stack.md` before adding dependencies, changing Python tooling, or introducing packaging/build configuration.
- Keep changes scoped to the requested behavior.
- Prefer existing project patterns once they exist.
- Avoid unrelated refactors.

Maintainability expectations:

- Favor readable, maintainable code over clever or overly abstract code.
- Use architecture patterns such as hexagonal architecture, dependency injection, SOLID, and DRY pragmatically, only when they make the code easier to understand, test, or change.
- Use design patterns as inspiration when they clarify intent, reduce real complexity, or make behavior easier to test and change. Do not introduce a pattern only to satisfy a named style.
- Avoid adding framework-style ceremony before the project needs it.
- If an implementation choice creates a meaningful tradeoff between readability, maintainability, simplicity, performance, or extensibility, pause and ask for a human decision before proceeding.

Architecture expectations:

- The MVP uses a pragmatic hexagonal architecture vocabulary: `cli`, `application`, `domain`, `ports`, and `adapters`.
- Because this repository contains one application, prefer top-level source directories under `src/` such as `src/cli`, `src/application`, `src/domain`, `src/ports`, and `src/adapters` instead of nesting everything under an application-name package.
- Keep core application workflow code separate from infrastructure concerns such as CLI parsing, local files, model downloads, and Whisper-specific transcription code.
- Treat ports as the interfaces or protocols the application depends on, and adapters as concrete implementations connected to external systems.
- Prefer simple dependency injection through constructors or function parameters over a dependency injection container unless the project grows enough to justify one.
- Treat `architecture/` as product-specific design guidance and decisions, not as a rigid coding standards manual.

Contract-first TDD expectations:

- For new requirement work, start by understanding the whole epic and write or update a human-readable epic-level contract under `requirements/` before implementation. Stories in the same epic often share one public surface and should be considered together before story-level tests begin.
- After the requirement contract is clear, create the smallest source contract surface in `src/` that tests can import. Use real module names, function or class signatures, and explicit placeholder behavior such as `raise NotImplementedError`.
- Then write TDD-style unit tests under `tests/unit/` against that source contract surface, using story references such as `0.1.1` for focused red-green cycles. The first red phase should preferably fail because behavior is not implemented, not because imports or modules are missing.
- The red phase is a required human checkpoint. After creating stubs and failing tests, run the relevant tests, report the expected failing result, and stop. Do not replace `NotImplementedError` or implement production behavior until the human explicitly approves moving to the green phase.
- If the human says "execute the plan" for contract-first TDD work, treat that as permission to create or update the contract, source stubs, and failing tests only. It is not permission to implement the green phase unless they explicitly say to implement behavior or make the tests pass.
- If production behavior is accidentally implemented before the red checkpoint, stop as soon as the issue is noticed and ask whether to keep the implementation, revert to stubs, or continue from the current state.
- After the human approves the green phase, implement only enough production code to satisfy the current contract and tests, one story or narrow behavior at a time.
- Keep contract tests focused on observable behavior, validation, workflow dispatch, and clear errors. Avoid real model downloads, real transcription, or production file writes in unit tests.

Tech stack expectations:

- Use Python with `pip` and `venv` for the MVP unless an explicit decision changes that direction.
- Do not introduce Poetry, Pipenv, Conda, or another dependency manager without asking first.
- When starting new implementation work that touches Python tooling or dependencies, check whether a newer stable Python or `pip` version exists and prefer upgrading unless blocked by compatibility or an explicit project decision.
- Once dependencies exist, use `pip-audit` after dependency changes and report any audit that could not be run.

During implementation:

- Make model download behavior deterministic and testable.
- Keep file paths, generated outputs, and model configuration explicit.
- Use logging intentionally with appropriate levels: `DEBUG` for diagnostics, `INFO` for normal workflow milestones, `WARNING` for recoverable unusual conditions, `ERROR` for operation failures, and `CRITICAL` only when the application cannot continue safely.
- Handle missing files, invalid timestamps, unavailable models, and failed downloads with clear errors.
- Do not silently discard generated captions, review data, or correction memory.

Before finishing:

- Run relevant tests or verification scripts.
- Report what changed and what was verified.
- State any verification that could not be run.

