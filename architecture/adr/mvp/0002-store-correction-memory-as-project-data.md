# ADR 0002: Store Correction Memory as Project Data

## Status

Accepted

## Date

2026-06-05

## Requirement References

- `2.1` - Vocabulary Correction
- `2.2` - Caption Cleanup
- `2.3` - Caption Export

## Context

Fast Video Captioning is built around a human-reviewed caption workflow. The product should produce clean captions, a human review file, and correction memory that can improve future captioning runs.

Correction memory is part of the value of the product: recurring names, phrases, channel vocabulary, and transcript fixes should become reusable knowledge. If this data is hidden as an implementation side effect, users cannot audit it, correct it, back it up, or intentionally improve it.

The current MVP requirements already make channel vocabulary explicit through files such as `local/vocab.csv` and optional cleanup inputs such as `local/blacklist.config`.

## Decision

Correction memory will be treated as explicit project data, not as an opaque side effect.

The application must preserve generated captions, review data, and correction memory in user-visible files or directories. Correction memory should be readable, auditable, and reusable across captioning runs.

Implementation should follow these rules:

- Do not silently discard generated captions, review data, or correction memory.
- Keep correction memory paths explicit and configurable where appropriate.
- Prefer simple, inspectable formats for correction data.
- Report missing, invalid, or unreadable correction data with clear errors.
- Make future correction-memory updates testable through file input and output behavior.

## Consequences

Caption quality can improve over time through a transparent review loop.

The application needs clear ownership of generated output files, review artifacts, and correction memory files.

Tests should verify that correction data is loaded, validated, applied, saved, and preserved without hidden state.

Future changes that introduce databases, embeddings, or automated learning should preserve an auditable export or source-of-truth representation unless a new ADR supersedes this decision.
