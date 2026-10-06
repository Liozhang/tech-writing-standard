---
name: tech-writing-standard
description: >
  Write, review, and audit product technical documentation against the General
  Technical Documentation Writing Standard, version 1.2. The standard is built
  on the ISO 24495-1 plain-language principles and IEC/IEEE 82079-1 preparation
  of information for use. It ships two language modules (Simplified Chinese and
  English), four domain extensions (aerospace and defence, medical, mechanical,
  software), a concept-first termbase, and four executable gate scripts for
  Chinese sentence length, English sentence length, accessibility, and term
  consistency. Output is a revision list sorted into must-level violations,
  should-level violations, and items needing human review, plus a conformance
  level verdict. Use when the user asks to write or revise product manuals,
  user guides, software documentation, operations runbooks, or training
  material; to review or polish technical documentation; to check documents
  against a writing standard; to run gate checks; to reconcile terminology; to
  author a new language module; or mentions plain language, ASD-STE100,
  Simplified Technical English, ISO 24495-1, or documentation conformance. Not
  for research papers, theses, marketing copy, or other publication-oriented
  writing, and not for languages other than Simplified Chinese and English.
allowed-tools: Bash Read Write Edit Glob Grep
metadata:
  version: "1.2"
  license: MIT
---

# tech-writing-standard

An executable technical writing standard, not a list of writing tips.

The rules are organised in three layers: generic rules that hold for every
language, one language module per language, and one domain extension per
industry. Two outputs separate this skill from general writing assistants.
Rules are machine-checkable through four gate scripts. Conformance is
declarable through three levels.

## When to use

Use this skill when any of these tasks appears:

- Drafting product manuals, user guides, software documentation, operations
  runbooks, or training material.
- Reviewing or polishing existing technical documentation.
- Auditing a document set and producing an actionable revision list.
- Building a termbase for a project.
- Authoring a language module for a language that has none yet.
- Producing documentation that must survive constrained delivery, such as
  black-and-white printing, offline single files, or low-literacy readers.

## When not to use

Do not use this skill for these cases, and say so explicitly:

- Publication-oriented research writing: journal papers, theses, preprints,
  systematic reviews, study protocols, data management plans, grant
  applications. These follow national standards and the rules of the target
  journal or academic community.
- Creative writing, marketing copy, formal legal text.
- Languages other than Simplified Chinese and English. Those languages have
  only a module-writing guide.
- Declaring full-level conformance. Human comprehension testing and
  screen-reader testing are still open, so no document may claim that level.

## Where the rules live

Read what the task needs. Do not read every file at once. English summaries
sit in `references/`. The authoritative text for the Chinese module and the
review record stays in `references/zh-Hans/`.

| File | Contents | Read it when |
|---|---|---|
| references/01-charter.md | Scope, five principles, conformance levels, conflict order, definitions | Starting any task |
| references/02-generic-rules.md | Language-neutral core rules GEN-001 to GEN-073 | Starting any task |
| references/03-module-zh-hans.md | Simplified Chinese rules ZH-001 to ZH-027 and parameter table | Document is in Simplified Chinese |
| references/04-structure-and-delivery.md | Information structure, metadata, versioning, release, accessibility STR-001 to STR-053 | Structure or delivery is involved |
| references/zh-Hans/00-索引与定位.md | Full Chinese index, revision history, stated limitations | Verifying version or tracing history |
| references/zh-Hans/05-语言模块-英语.md | English module rules EN-001 to EN-107, including the high-safety variant | Document is in English |
| references/zh-Hans/06-语言模块-编写指南.md | How to author a new language module, bidirectional text rules | A new language is needed |
| references/zh-Hans/07-领域扩展.md |追加 requirements for aerospace and defence, medical, mechanical, software | Document belongs to one of those four domains |
| references/zh-Hans/09-术语库规范.md | Concept-first multilingual termbase management TERM-001 to TERM-040 | Building or maintaining a termbase |
| references/zh-Hans/10-工具链与度量规范.md | Automated checking and comprehension testing TOOL-001 to TOOL-072 | Running checks or acceptance |
| references/zh-Hans/11-标准映射矩阵.md | Which source standard each rule comes from | Justifying a rule |
| references/zh-Hans/17 to 19 | Conformance drill report, full-level closure record, human test manual | Full-level evidence or test protocol is needed |

Review and dry-run records 12 to 16 are distributed in `references/zh-Hans/`
for traceability. They are historical, not operative.

## Workflow

### Step 1. Decide the conformance level

Read `references/01-charter.md` section four. Three levels exist: full,
reviewed, and adapted. Safety-critical and regulated documents take the level
set by the domain extension and cannot be lowered. Write the level into the
document metadata, and never lower it afterwards.

### Step 2. Load the three rule layers

Apply the layers from generic to specific:

1. Generic rules. Read `references/02-generic-rules.md`. They apply to every
   document.
2. Language module. Read `references/03-module-zh-hans.md` for Simplified
   Chinese or `references/zh-Hans/05-语言模块-英语.md` for English. If the
   language has no module, read `references/zh-Hans/06-语言模块-编写指南.md`.
3. Domain extension. Read `references/zh-Hans/07-领域扩展.md` and apply only
   the extension for the document's industry.

When layers conflict, apply the seven-level order in
`references/01-charter.md`: law and regulation, contract and customer
specification, journal or community rules, domain extension, language module,
generic rules, principles.

### Step 3. Write or revise

These requirements come up most often:

- One idea per sentence. Respect the sentence-length limits of the language
  module.
- Safety content never scales down. Keep the signal word, hazard, consequence,
  and countermeasure, and keep the warning before the step it applies to.
- Follow the termbase. One concept uses one approved form; banned forms are
  never used.
- Sort content into the five information types: concept, task, reference,
  tutorial, troubleshooting. Decide the type before writing.

### Step 4. Run the four gate scripts

Run one mode at a time from the skill's `scripts/` directory:

```
python scripts/doccheck.py <file-or-dir> 50
```

| Mode | Command | Checks | Boundary |
|---|---|---|---|
| Default | `python scripts/doccheck.py <target> 50` | Chinese sentence length, mixed-script spacing, heading jumps, rule level field | Machine-checkable subset only; table rows are counted as layout, not violations |
| English | `python scripts/doccheck.py <target> --en` | English sentences over 25 words, parenthetical lists counted separately | Sentences needing the ASD-STE100 variant need a separate judgement |
| Accessibility | `python scripts/doccheck.py <target> --a11y` | Image alternative text, table header rows, empty link text | Contrast and focus order need measurement |
| Terms | `python scripts/doccheck.py <target> --term` | Banned terms and synonym mixing | Reads `scripts/termbase.csv`; pass `--termbase <path>` to use another termbase |

The second argument of the default mode is the descriptive sentence limit,
50 characters by default. Re-check operation sentences against the tighter
limit in the language module.

### Step 5. Report and revise

Report findings in three separate groups:

1. Must-level violations. Give file, line, rule number, and a concrete
   rewrite.
2. Should-level violations. Give the reason and the waiver condition.
3. Items the scripts cannot see. Terminology ambiguity, semantic
   completeness, and real-device procedure order belong here.

Re-run the gates until must-level violations reach zero. The gate scripts are
an aid, not a verdict. A clean run does not make a document adequate.

### Step 6. Full-level handling

For full-level conformance, read
`references/zh-Hans/19-真人测试与阈值实测操作手册.md`. Five items require
real people: comprehension testing, screen-reader testing, termbase project
validation, translation margin measurement, and constrained-delivery
thresholds. Simulated readers and language models cannot replace real people,
and proxy evidence must not close gates that need them. These items are open,
so no document may claim full-level conformance.

## Conformance and module status

| Item | Current status |
|---|---|
| Full level | Closed. Do not claim it |
| Reviewed level | Available, Simplified Chinese and English modules |
| Adapted level | Available, Simplified Chinese and English modules |
| Simplified Chinese module | Reviewed level, four gates pass, 27 unit tests pass |
| English module | Reviewed level, English gate passes |
| Other languages | Guide level only |

## Hard boundaries

- Gate scripts are an aid. Never equate a clean run with an adequate document.
- Never claim evidence you do not have. Gates that need a human close only
  with human evidence.
- Regulated documents require checking against current target-market
  regulation. This standard governs the writing layer only and is not proof of
  product compliance.
- Referenced standards follow their current effective edition. Verify the
  edition before adoption.
- The scripts ship 27 unit tests. After changing a script, re-run the tests,
  then re-run the four gates.

## Known limits

- The scripts cover prose-type Chinese documents. Code blocks, inline code,
  commands, and paths are excluded by rule.
- Table rows, logs, and machine-generated scans are not counted as sentence
  violations.
- Semantic rules are not implemented: information completeness, procedure
  correctness, and safety adequacy all require human review.
- The term gate depends on the termbase. Word forms outside the termbase are
  never flagged.
