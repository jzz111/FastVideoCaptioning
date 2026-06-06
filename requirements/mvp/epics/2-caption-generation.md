# Epic 2: Caption Generation

## Feature 1: Vocabulary Correction

### Story 1: Apply vocabulary corrections to transcript
#### Description
The application will load a CSV that will have 2 columns: 

| key | value | 
| --| -- |
| Correct Term | Transcript Variant |

The application will replace all instances of `value` with `key` across the entire text. Every row will be applied. The file will, by default, live in the local at `local/vocab.csv`. The user can, alternately, specify another location via command line argument.

#### Acceptance Criteria
- Load vocabulary CSV
- Validate vocabulary dictionary
- Handle missing vocabulary file
- Handle invalid vocabulary entries


## Feature 2: Caption Cleanup

### Story 1: Format caption text

#### Description
The formating will happen in the following steps:

Step 1:
A blacklist vocabulary file will be read. Any matching entries will be removed from the transcript. The file will, by default, live in the local at `local/blacklist.config`. The user can, alternately, specify another location via command line argument.

Step 2:
The application will take a text file with the exported marker (for YouTube timeline chapters) and divide the caption into paragraphs using it, marking the start of each marker as a new paragraph. The format of the marker looks like `{{timecode}} - {{comment}}` in kdenlive. A sample marker export looks like:

```
0:00 - Intro
0:20 - Overview
1:52 - Results
3:59 - Imperfect Environment
8:43 - Analysis of Results
11:30 - Conclusion
```
This file will be a required argument in the command line arguments.

#### Acceptance Criteria
- Preserve caption readability
- Handle reading "blacklist vocabulary". This file is optional.
- Handle reading marker export file
- Handle non-existence for marker export file
- Handle formatting failures
- Reduce all repeating whitespaces to just one space before paragraphing is applied


## Feature 3: Caption Export

### Story 1: Export caption output as TXT

#### Description
The export file location must be specified in the command line argument.

#### Acceptance Criteria
- Handle missing command line argument for export file location
- Handle export failures
