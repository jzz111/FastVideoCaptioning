# Requirements

This directory contains the product and MVP requirements for Fast Video Captioning. Start here when you need to understand what the project is trying to build before writing tests or implementation code.

## How to Navigate

Read the docs from broad product intent to specific implementation work:

1. `product-vision.md` - Explains the purpose of the product and the role of human review.
2. `product-users.md` - Defines the primary and secondary users and what they need.
3. `product-workflow.md` - Shows the full product workflow from upload through feedback storage.
4. `mvp/product-mvp-roadmap.md` - Narrows the full product into the MVP workflow, epics, and future ideas.
5. `mvp/epics/` - Contains the detailed MVP requirements that should drive tests and implementation.

## Directory Map

```text
requirements/
|-- product-vision.md
|-- product-users.md
|-- product-workflow.md
`-- mvp/
    |-- product-mvp-roadmap.md
    `-- epics/
        `-- detailed MVP epic requirement docs
```

## What Each Area Is For

| Area | Purpose | Use it when |
| --- | --- | --- |
| Product docs | Describe the overall product intent, users, and workflow. | You need context for why a feature exists or what outcome it should support. |
| MVP roadmap | Defines the first buildable version of the product. | You need to decide what belongs in the MVP versus a future release. |
| MVP epics | Break the MVP into features, stories, descriptions, and acceptance criteria. | You are writing tests, planning implementation, or checking whether a feature is complete. |

## Epic Doc Shape

Epic docs are organized to move from high-level scope into testable behavior:

```text
Epic
Feature
Story
Description
Acceptance Criteria
```

Acceptance criteria should be treated as the source of truth for test design. If a requirement is unclear, update the relevant requirement doc before implementing the behavior.
