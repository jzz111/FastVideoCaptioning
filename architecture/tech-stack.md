# Tech Stack

This document records the current technical defaults for Fast Video Captioning.

It is a living architecture reference, not a permanent contract. When a tool choice becomes important enough to explain why one option was chosen over another, record that decision in an ADR.

## Current Defaults

| Area | Default |
| --- | --- |
| Language | Python |
| Dependency management | `pip` with `venv` |
| Dependency audit | `pip-audit` once Python dependencies exist |
| Architecture style | Pragmatic hexagonal architecture |
| Default captioning model | OpenAI Whisper Large-v3 |
| Alternate captioning model | OpenAI Distil-Whisper |

## Python And Pip Currency

When starting new implementation work, check whether a newer stable Python or `pip` version exists.

If the local project version is behind the latest stable version, prefer upgrading before adding new code unless a dependency, operating system constraint, or explicit project decision prevents it.

This matters for security as much as convenience. Old runtimes and package tooling can contain serious vulnerabilities, and dependency work should not build on a stale foundation by accident.

Version upgrades should be deliberate:

- Confirm the target version is stable, not prerelease.
- Check whether existing dependencies support the target version.
- Run relevant tests or verification after upgrading.
- Record meaningful version-policy decisions in an ADR when they affect the MVP or future releases.

## Dependency Management

Use `pip` and `venv` for the MVP unless a stronger packaging need emerges.

Do not introduce Poetry, Pipenv, Conda, or another dependency manager without a deliberate decision. Extra tooling can be useful, but it should solve a real project problem rather than appear by default.

Prefer explicit dependency files once dependencies exist:

- `requirements.txt` for runtime dependencies.
- `requirements-dev.txt` for development and verification tools.

## Dependency Auditing

Run `pip-audit` once Python dependencies exist and after dependency changes.

Dependency auditing should be treated as practical security hygiene for the MVP. It is not a full security program, but it helps catch known vulnerable packages before they become part of normal development.

## Deferred Choices

These choices should be made when implementation needs them:

- Test framework.
- CLI parsing library.
- Logging configuration.
- Formatter and linter.
- Packaging and build configuration.
