# Design Principles

Fast Video Captioning is a practical tool before it is an architecture exercise.

The goal is not to prove that a particular pattern can be implemented in Python. The goal is to build a captioning workflow that a creator can trust: inputs are clear, generated output is easy to review, corrections are preserved, and future runs can improve because the project remembers what the human fixed.

These principles describe the taste of the codebase. They are not a coding standards manual.

## Readability Is Product Quality

Readable code matters because this product is built around human review and correction. If the implementation hides what happened, the product becomes harder to trust.

A developer should be able to follow a captioning run and understand where the media came from, which model was used, what text was generated, what corrections were applied, and where every output file went.

That does not mean every function must be tiny or every concept needs a class. It means the shape of the code should make the workflow visible.

## Testability Is A Design Constraint

Fast Video Captioning should be built with test-driven development in mind.

Tests are not just a safety net after implementation. They are part of how requirements become executable, reviewable behavior. A feature is easier to trust when its acceptance criteria can be seen in tests and those tests can run without depending on fragile external state.

The core workflow should be testable without downloading real models, processing large media files, or writing production output. External systems such as Whisper, the filesystem, model registries, and command line input should be replaceable with focused test doubles when the behavior under test does not require the real thing.

Testable code usually has clearer boundaries. If a behavior is difficult to test, that may be a signal that the design is hiding too much work in one place.

## Debuggability Matters

Caption generation has several moving parts: media input, timestamps, model selection, transcription, vocabulary correction, cleanup, review output, and correction memory.

When something goes wrong, the code should help a developer understand where it went wrong.

Important decisions and failure points should be visible through clear errors, explicit file paths, named model configuration, and workflow steps that can be inspected independently. The implementation should avoid hidden fallbacks and swallowed exceptions because they make caption output harder to trust.

Good debuggability does not require noisy logging everywhere. It requires enough structure and context that a failure can be traced without guessing.

## Logging Should Explain The Workflow

Logging should help a developer or operator understand what the application did, what it decided, and where it failed.

Good logging is not the same as more logging. The useful log is the one that gives enough context to diagnose a problem without exposing unnecessary noise or making normal runs feel alarming.

Use log levels intentionally:

- `DEBUG` for detailed diagnostic information that helps during development or deep troubleshooting.
- `INFO` for normal workflow milestones, such as selected model, input file accepted, transcript generated, captions exported, or correction memory updated.
- `WARNING` for recoverable problems or unusual conditions that the application can handle, such as an optional vocabulary file being absent.
- `ERROR` for failures that prevent the requested operation from completing, such as missing required files, invalid timestamps, unavailable models, failed downloads, transcription failure, or output write failure.
- `CRITICAL` for failures that indicate the application cannot continue safely at all. This should be rare.

Logs should include useful identifiers such as file paths, model names, output locations, and workflow step names when those details help explain the run. Logs should not hide failures behind vague messages, and they should not silently replace clear user-facing errors.

## Patterns Are Tools, Not Proof

This project can benefit from hexagonal architecture, domain-driven design, dependency injection, SOLID, DRY, and named design patterns. Those ideas are useful when they help us separate concerns, test behavior, and explain intent.

They are less useful when they become ceremony.

The project should use the smallest version of a pattern that solves a real problem. A simple constructor argument may be enough dependency injection. A Python protocol may be enough interface. A plain function may be better than a new class.

The pattern is successful when the next change is easier to make and the current code is easier to read.

## Product Language Should Show Up In Code

The code should sound like the product.

Concepts such as `MediaClip`, `Transcript`, `CaptionDocument`, `ReviewFile`, `CorrectionMemory`, `VocabularyCorrection`, and `TranscriptionModel` are useful because they are real things in the workflow. They help the implementation stay connected to what the user is doing.

Artificial names are a warning sign. If a class or module name only describes a layer, utility bucket, or vague technical role, it may be hiding the product concept that actually matters.

## Tradeoffs Should Be Conscious

Most implementation choices can be made locally. Some choices affect the character of the product.

Those deserve a human decision.

Examples include choosing a faster approach that makes output harder to audit, adding a broad abstraction before the MVP needs it, taking on a dependency that complicates setup, or choosing a storage format that is convenient for code but awkward for a human to inspect.

When a choice changes the balance between readability, maintainability, simplicity, performance, and extensibility, the tradeoff should be named rather than smuggled into the code.

## Human Review Is Not An Afterthought

The review loop is part of the product promise.

Generated captions are not disposable scratch output. Review files and correction memory are not invisible implementation details. They are how the creator checks the work, teaches the tool, and gets better results over time.

Architecture decisions should protect that loop. The system should make review artifacts and correction memory visible, auditable, and recoverable.
