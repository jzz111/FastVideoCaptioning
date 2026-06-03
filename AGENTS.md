# Repository Instructions

## Project Purpose

Fast Video Captioning demonstrates using AI to generate captions for videos while keeping human ownership over the output and the development process.

The application workflow centers on:

- Accepting a video or audio file.
- Using clip start and end timestamps.
- Optionally applying channel-specific vocabulary.
- Producing clean `.txt` captions.
- Producing a human review file.
- Maintaining correction memory.

## Product Capabilities

The finished product must be able to download captioning models needed for transcription and caption generation.

Current supported model options are:

- OpenAI Whisper Large-v3 as the default model.
- OpenAI Distil-Whisper as an alternate model.

## Development Principles

Human ownership is required for all AI-generated work. Treat AI as a tool that can accelerate implementation, but the developer is responsible for reviewing, refining, testing, and owning every requirement, plan, and line of code.

Prefer a requirements-and-tests-first workflow:

1. Maintain repository context in this `AGENTS.md` file.
2. Write or update requirement specifications before feature work.
3. Design tests from the requirements before implementation when the work is a feature or larger.
4. Use Plan Mode for code generation on meaningful changes.
5. Add automated verification scripts or tests so manual checks are not the only safety net.

## Workflow Levels

For simple bug fixes:

- Use this context file.
- Implement the fix.
- Run or add automated verification.

For features:

- Use this context file.
- Define requirements and acceptance criteria.
- Create or update tests first.
- Implement through a reviewed plan.
- Run automated verification.

For major features:

- Use the complete workflow: context, requirements, tests, planned implementation, and automated verification.

## Requirements Guidance

Feature requirements should include acceptance criteria. Gherkin is acceptable when useful, but plain language is fine if the success conditions are precise and testable.

Requirements should come from, or at minimum be reviewed by, the Product Owner or Product Manager.

## Testing Guidance

Tests are safeguards around AI-assisted development. For feature work, design tests from the acceptance criteria before implementation.

Unit tests created for feature behavior should be peer reviewed so the team owns the expected behavior, not just the generated implementation.

When adding automated testing tools, prefer repeatable scripts that create technical equity over one-time manual test steps.

## Implementation Guidance

Before changing code:

- Read the relevant requirements, README, and existing code.
- Keep changes scoped to the requested behavior.
- Prefer existing project patterns over new abstractions.
- Avoid unrelated refactors.

During implementation:

- Make the smallest coherent change that satisfies the requirements.
- Keep generated captions, review outputs, and correction memory behavior understandable and auditable.
- Preserve human review as a first-class part of the captioning workflow.

Before finishing:

- Run the relevant tests or verification scripts.
- Report what changed and what was verified.
- Clearly state any tests that could not be run.
