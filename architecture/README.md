# Architecture

This directory records the durable technical guidance for Fast Video Captioning.

Use it for decisions, design principles, coding patterns, and workflow conventions that should outlive a single implementation task.

## Directory Map

```text
architecture/
|-- application-architecture.md
|-- design-principles.md
|-- tech-stack.md
|-- patterns/
|   `-- python-implementation-patterns.md
`-- adr/
    `-- mvp/
        `-- MVP architecture decision records
```

## What Belongs Here

| Area | Purpose |
| --- | --- |
| `adr/` | Records decisions with context, options, consequences, and status. |
| Design principles | Stable guidance for how the product should behave and feel. |
| Tech stack | Current technical defaults and dependency-management guidance. |
| Coding patterns | Project-specific implementation conventions once they emerge. |
| Data flow docs | Explanations of how media, transcripts, captions, review data, and correction memory move through the system. |

ADRs are for decisions where the project chose one direction over other plausible options. General coding style, naming conventions, and implementation patterns can be regular architecture docs unless they record a specific decision.

Version- or milestone-specific ADRs should live in a matching subdirectory such as `adr/mvp/`.

Start with:

- `design-principles.md` for maintainability and tradeoff guidance.
- `application-architecture.md` for the product's preferred architecture shape.
- `tech-stack.md` for current technical defaults and dependency hygiene.
- `patterns/python-implementation-patterns.md` for pragmatic Python conventions.
