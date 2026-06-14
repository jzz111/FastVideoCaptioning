# Fast Video Captioning

## Table of Contents
- [Fast Video Captioning](#fast-video-captioning)
  - [Table of Contents](#table-of-contents)
  - [What this is](#what-this-is)
  - [Tool Usage](#tool-usage)
    - [Input:](#input)
    - [Output:](#output)
  - [Directory Structure](#directory-structure)
  - [Demonstrated Workflow](#demonstrated-workflow)
    - [Overview](#overview)
      - [Steps in the process](#steps-in-the-process)
      - [Levels of operation](#levels-of-operation)
    - [1. AGENTS.md](#1-agentsmd)
    - [2. Requirement Specification](#2-requirement-specification)
    - [3. Design Unit Tests](#3-design-unit-tests)
    - [4. Generate code in Plan Mode](#4-generate-code-in-plan-mode)
    - [5. Generate Automated Testing Tools](#5-generate-automated-testing-tools)

## What this is
This is a code base to demonstrate using AI to generate an automatic way to caption videos for content creators. As the creator behind "Vibe Gardening: Informed Edition", a gardening channel on YouTube, I have a constant need of captioning my videos. The current workflow offered in kdenlive for captioning my video creates a large overhead in my publishing process. This app will both serve as a tool to help teach responsible AI use as well as solving a pain point in my operations.

## Tool Usage
### Input:
- Video/audio file
- Clip start/end timestamps
- Optional channel vocabulary

### Output:
- Clean .txt captions
- Human review file
- Correction memory

## Directory Structure
```text
FastVideoCaptioning/
|-- AGENTS.md
|-- LICENSE
|-- README.md
|-- architecture/
|   |-- architecture decisions and technical guidance
|-- requirements/
    |-- product requirement docs
```

| Path | Description | What it looks like |
| --- | --- | --- |
| `requirements/` | Product requirement docs that describe the users, product vision, and expected workflow. | Short Markdown files with headings, numbered workflow steps, and bullet lists. |
| `architecture/` | Technical guidance and Architecture Decision Records that explain important implementation choices. | Markdown files describing decisions, consequences, and project conventions. |


## Demonstrated Workflow
### Overview
As the human behind AI operations, you must own what the AI generates. This workflow brings ownership back to humans for what the AI produces. It also gives humans the control they need to own every step of the development

#### Steps in the process
1. AGENTS.md construction for AI context
2. Requirement specification
3. Design TDD style unit tests using the requirements
4. Generate code using Plan Mode
5. Generate additional verification using automated testing scripts

#### Levels of operation
1. Simple problems, like bugfixes:    
   - Steps 1, 4, 5
2. Features: 
   - Steps 1, 3, 4, 5
3. Major Features:
   - All Steps

### 1. AGENTS.md
This is the pillar of AI development to give the AI context of how you want this workspace/project to behave.

### 2. Requirement Specification
You will need to specify the requirements that this feature/application must meet to be considered a success. This can be written in styles like Gherkin or other languages. Acceptance Criterias are a must as they drive the TDD step. This needs to be from the Product Owner or Product Manager, at least reviewed by.

### 3. Design Unit Tests
Due to AI's role as a tool, it must be constrained using safeguards. TDD is the best approach to develop such safeguards. These unit tests developed MUST be Peer Reviewed (PRed) by the team to ensure team ownership.

### 4. Generate code in Plan Mode
The developer must read every word the AI generates in the Plan of how it will implement ... the developer must remember that every line of the code generated will be owned by them. The plan must be refined until the developer deems it a success.

### 5. Generate Automated Testing Tools
The developer/team will also generate scripts to automate the testing of the code developed by Step 4. Manual testing works but it will have to be redone. We must automate testing so we can gain technical equity from what we do.
