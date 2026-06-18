# Fast Video Captioning

Fast Video Captioning is a caption-generation project for content creators. It turns source video or audio into clean captions that can be reviewed, corrected, and reused to improve future captioning runs.

This repository also demonstrates a human-owned AI development workflow. The goal is not just to generate code quickly, but to keep product intent, requirements, contracts, tests, implementation, and verification visible to the people who own the system.

## Table of Contents

- [What This Is](#what-this-is)
- [Tool Usage](#tool-usage)
- [Directory Structure](#directory-structure)
- [Demonstrated Workflow](#demonstrated-workflow)

## What This Is

This project started from a real captioning need for the YouTube channel "Vibe Gardening: Informed Edition." The existing captioning workflow in Kdenlive adds friction to the publishing process, so this application is intended to reduce that overhead while keeping human review central.

The product should produce useful captions for content creators, support auditable review files, and preserve correction memory as project data rather than an invisible side effect.

## Tool Usage

### Inputs

- Video or audio file
- Clip start and end timestamps
- Optional channel-specific vocabulary for names, phrases, jargon, or recurring terms

### Outputs

- Clean `.txt` captions
- Human review file for checking and correcting generated captions
- Correction memory that can improve future captioning runs

## Directory Structure

```text
FastVideoCaptioning/
|-- AGENTS.md
|-- LICENSE
|-- README.md
|-- architecture/
|-- requirements/
|   `-- mvp/
|       `-- contracts/
|           `-- human-readable requirement contracts
|-- src/
`-- tests/
    `-- unit/
```

Requirement contracts live in `requirements/mvp/contracts/`. These contracts describe the public behavior expected from a feature before production implementation begins.

Unit tests live in `tests/unit/`.

## Demonstrated Workflow

### Overview

As the human behind AI-assisted development, you must own what the AI generates. This workflow keeps ownership with humans by making intent, acceptance criteria, tests, code, and verification explicit.

### Steps In The Process

1. Construct AI context.
2. Define the product specification.
3. Design contract-first, TDD-style unit tests from the requirements.
4. Generate code through a reviewed implementation plan.
5. Generate automated verification tools.

### Levels Of Operation

1. Simple problems, such as bug fixes: steps 1, 4, and 5.
2. Features: steps 1, 3, 4, and 5.
3. Major features: all steps.

### 1. Construct AI Context

`AGENTS.md` is the main source of AI development guidance for the workspace. It defines how the project should behave, how work should be scoped, and what expectations the AI assistant should follow.

The `architecture/` directory contains architectural patterns, decisions, and technical guidance that help steer implementation choices.

### 2. Product Specification

The `requirements/` directory defines what the product and its features must do to be considered successful. Requirements should include clear acceptance criteria because those criteria drive the contract-first TDD process.

Product requirements should come from, or at least be reviewed by, the product owner or product manager.

### 3. Contract-First TDD

AI is a tool, and it needs safeguards. Contract-first TDD provides those safeguards by defining expected behavior before production code is implemented.

For new requirement work:

1. Define or update a human-readable contract as a Markdown file.
2. Create the smallest source contract surface that tests can import.
3. Use explicit placeholder behavior, such as `NotImplementedError`, until implementation is approved.
4. Write failing unit tests against the source contract.
5. Stop at the red phase for human review before implementing behavior.

These tests should be peer reviewed so the team owns the behavior being protected.

### 4. Generate Code Through An Implementation Plan

The developer must read and refine the AI-generated implementation plan before code is written. Every generated line becomes the developer's responsibility, so the plan should be treated as a design artifact worth reviewing.

### 5. Generate Automated Verification Tools

The team should automate verification whenever practical. Manual checks are useful, but automated tests and scripts create repeatable confidence and reduce the cost of future change.
