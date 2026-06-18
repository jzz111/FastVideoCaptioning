# Python Implementation Patterns

Fast Video Captioning should use Python patterns that support readable, testable code without importing unnecessary framework habits.

## Modules and Boundaries

Prefer modules that match product responsibilities.

Possible future source layout:

```text
src/
|-- cli/
|   |-- models/
|   |-- ports/
|   |-- services/
|   `-- command_line.py
|-- application/
|   |-- models/
|   |-- ports/
|   `-- workflows/
|-- domain/
|   `-- models/
`-- adapters/
```

Because this repository contains one application, avoid adding an extra application-name package layer unless a future packaging decision requires it. This layout is a direction, not a requirement. Introduce directories when implementation work needs them.

Top-level boundary packages such as `cli`, `application`, `domain`, and `adapters` should hold entry points or cohesive subpackages. Put model classes, request or result types, protocols, workflow contracts, and behavioral services in named subpackages such as `models`, `ports`, `workflows`, or `services` instead of collecting several classes or helper behaviors in one orchestration file.

Prefer one primary class, protocol, or type alias per file when it represents a contract, model, request, result, or domain concept. Small private helper functions may stay in the module they support.

Entry point modules should stay small. Move parsing, validation, rendering, formatting, and workflow dispatch behavior into focused service modules once an entry point starts accumulating helper functions.

Prefer cohesive service modules with functions over static-style utility classes. Add a class when it represents state, a replaceable dependency, a protocol implementation, or a concept that becomes clearer as an object.

## Contract-First TDD

Use a contract-first TDD flow for requirement work.

1. Start from the whole epic, such as Epic `0`, before writing story-level tests.
2. Write or update the human-readable behavior contract under `requirements/`.
3. Add the smallest importable source contract surface under `src/`.
4. Use explicit placeholders such as `raise NotImplementedError` for behavior that has not been implemented.
5. Write unit tests under `tests/unit/` against the source contract.
6. Run the relevant tests and confirm the expected red result.
7. Stop for human review and approval before implementing behavior.
8. After approval, implement only enough production behavior to make the current tests pass.

Contract discovery should happen at the epic level because stories in the same epic usually share a public surface, naming scheme, validation rules, and workflow boundaries. For example, Epic `0` describes one connected CLI contract even though its help, validation, caption dispatch, and model-management dispatch behaviors can be tested and implemented story by story.

After the epic-level contract is clear, use story references such as `0.1.1` to drive focused red-green implementation cycles. The epic contract gives the shape; the story tests decide the next small behavior to implement.

The initial red phase should usually fail because the source contract raises `NotImplementedError`, not because the module, function, or class does not exist.

The red phase is a required review checkpoint. Creating the contract, stubs, and failing tests is a complete TDD step by itself. Do not move from red to green until the project owner explicitly approves implementation. A broad instruction such as "execute the plan" should be interpreted as permission to reach the red checkpoint, not as permission to implement production behavior, unless implementation is explicitly requested.

If production behavior is accidentally implemented before the red checkpoint, stop as soon as the mistake is noticed. Ask the project owner whether to keep the implementation, revert to stubs, or continue from the current state.

This keeps tests tied to real project names and boundaries while preserving the discipline that behavior is specified before it is implemented.

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

Unit tests should mirror the `src/` boundary structure for behavioral units. For example, source code in `src/cli/command_line.py` should be tested under `tests/unit/cli/`, `src/cli/services/argument_parser.py` should be tested under `tests/unit/cli/services/`, and future source code in `src/application/workflows/` should be tested under `tests/unit/application/workflows/`.

Keep public contract tests distinct from focused unit tests. Contract tests protect user-visible behavior and requirement references at a boundary such as the CLI. Focused service tests protect smaller behavioral units such as parsing, validation, rendering, formatting, and dispatch.

Name test files after the source surface or contract they protect, such as `test_command_line_contract.py`. Keep test helpers close to the tests that use them until shared test support becomes necessary.

When using Python `unittest` discovery with mirrored package names, keep any test package `__init__.py` files minimal and only use them to support discovery or source-package resolution.

Do not create unit tests solely for passive dataclasses, constants, type aliases, or protocols. Cover those indirectly through the behavioral services and public contract tests that use them. Add direct model tests only when a model gains validation, normalization, computed behavior, or other logic.

Prefer fake adapters or temporary files over real model downloads in unit tests. Model download behavior should be deterministic and testable without requiring network access unless the test is explicitly an integration test.
