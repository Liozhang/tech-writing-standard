# tech-writing-standard

An executable standard for product technical documentation, with four gate
scripts you can run.

Write a manual, then check it. The result is a revision list sorted into
must-level violations, should-level violations, and items that need a human.
Rules are traceable to international standards, and every claim about what the
standard can prove is stated as what it is: claimed, evidenced, or open.

- 中文入口见 [README.zh-CN.md](README.zh-CN.md)，技能中文版见
  [SKILL.zh-CN.md](SKILL.zh-CN.md)。

## Why this exists

Three recent developments pushed this project. Each one is a matter of public
record, and each one changes what a writing standard has to do.

**1. AI-generated content became a regulated object.** Since 2 August 2026 the
transparency obligations in Article 50 of the EU AI Act apply. AI-generated or
manipulated content must be identifiable, chatbot interactions must be
disclosed, and synthetic media must be labelled. Technical documentation is
increasingly drafted with language models. Content that a regulator can ask you
to identify cannot be content whose origin and revision trail nobody tracked.
The standard treats provenance and versioning as must-level requirements, not
as good practice.

**2. Code output outran document quality.** Teams using AI coding tools report
substantial throughput gains, with measured speedups of up to 55 percent in
some studies. Commentators writing about the 2026 developer toolchain repeat
the same warning: AI can produce incorrect assumptions, outdated approaches,
and plausible but wrong details. Code gets generated at speed while the manual
that explains it is either unwritten or also machine-drafted without review.
The standard answers this with machine-checkable gates, so a document can be
measured instead of merely read.

**3. Machine-generated prose needs machine-checkable rules.** CodeRabbit's
December 2025 analysis of AI versus human code generation found AI-generated
code to be more variable and more likely to introduce high-severity issues.
The same mechanism applies to prose: fluent output is not accurate output. A
standard whose rules cannot be checked produces documents that look compliant
and are not. Hence the design rule of this repository: if a rule matters, it
must have a number, a level, a check method, and a waiver path.

## What you get

| Part | What it does |
|---|---|
| Generic rules | 73 language-neutral rules, GEN-001 to GEN-073 |
| Language modules | Simplified Chinese ZH-001 to ZH-027, English EN-001 to EN-107 with a high-safety variant |
| Domain extensions | Aerospace and defence, medical, mechanical, software |
| Structure and delivery | Information structure, metadata, versioning, release, accessibility, constrained delivery, STR-001 to STR-053 |
| Termbase rules | Concept-first multilingual term management, TERM-001 to TERM-040 |
| Toolchain rules | Automated checking and comprehension testing, TOOL-001 to TOOL-072 |
| Gate scripts | Four modes: Chinese sentence length, English sentence length, accessibility, term consistency |
| Worked example | A bioinformatics runbook written under the standard, with its own termbase |

## Install as a ZCode skill

Copy this directory into your user skills folder:

```bash
cp -r tech-writing-standard ~/.zcode/skills/
```

`SKILL.md` is the English entry point. `SKILL.zh-CN.md` is the Chinese entry
point; ZCode loads `SKILL.md` by default, so to work in Chinese copy
`SKILL.zh-CN.md` over `SKILL.md` inside the installed directory.

## Use the gate scripts standalone

The scripts need only Python 3 and no third-party packages.

```bash
# Chinese sentence length, mixed-script spacing, heading jumps, rule levels
python scripts/doccheck.py <file-or-dir> 50

# English sentences over 25 words
python scripts/doccheck.py <file-or-dir> --en

# Accessibility items the machine can check
python scripts/doccheck.py <file-or-dir> --a11y

# Banned terms and synonym mixing
python scripts/doccheck.py <file-or-dir> --term
python scripts/doccheck.py <file-or-dir> --term --termbase <your-termbase.csv>
```

Run the unit tests:

```bash
python scripts/test_doccheck.py
```

26 tests, all passing as of version 1.2.

## Repository layout

```text
tech-writing-standard/
├── SKILL.md                  English skill entry point
├── SKILL.zh-CN.md            Chinese skill entry point
├── README.md                 This file
├── README.zh-CN.md           Chinese README
├── CHANGELOG.md
├── references/               English summaries of the operative rules
│   ├── 00-index.md
│   ├── 01-charter.md         Scope, principles, conformance levels, conflict order
│   ├── 02-generic-rules.md   GEN-001 to GEN-073
│   ├── 03-module-zh-hans.md  ZH-001 to ZH-027 and the parameter table
│   ├── 04-structure-and-delivery.md  STR-001 to STR-053
│   └── zh-Hans/              Authoritative Chinese text and full review record
├── scripts/                  Gate scripts, unit tests, demo termbase
└── examples/                 Bioinformatics runbook and its termbase
```

## Bilingual policy

English is the primary language of the skill and of the English rule summaries
in `references/`. Simplified Chinese is the authoritative language for the
Chinese language module, because ZH rules define Chinese sentence counting and
quoting conventions that do not survive translation. Both entry points
implement the same workflow and the same commands. When the two disagree on a
rule's content, the Chinese text in `references/zh-Hans/` wins, and the
disagreement is a defect to be reported.

## Conformance levels

| Level | What it demands |
|---|---|
| Full | Every must-level rule plus domain extensions, human comprehension testing, screen-reader testing, two-person review |
| Reviewed | Every must-level rule, should-level items waivable by review |
| Adapted | Every must-level rule, may-level items optional |

Full level is closed. Human comprehension testing, screen-reader testing, term
project validation, translation margin measurement, and constrained-delivery
thresholds are not done. No document may claim full-level conformance.

## Honest limits

- The gate scripts cover the machine-checkable subset only. Semantic rules,
  procedure correctness, and safety adequacy need human review.
- The scripts are prose-oriented. Code, commands, paths, and machine-generated
  output are excluded by rule.
- Table rows are counted as layout, not as sentence violations.
- The sentence limits for Simplified Chinese are informed by expert review and
  a percentile measurement on a 326-sentence corpus. Real-reader comprehension
  testing is not done, so those numbers are advisory, not certified.
- Simulated readers and language models are not evidence for gates that require
  real people.

## Sources the rules are traced to

ISO 24495-1, IEC/IEEE 82079-1, ASD-STE100, ISO 8601, the International System
of Units, ISO 15223-1, ISO 13485, ISO 12100, ISO 17100, ISO 30042, OASIS DITA,
W3C WCAG, GB/T 1.1, GB/T 15834, GB/T 15835, GB/T 16159. The mapping from each
rule to its source sits in `references/zh-Hans/11-标准映射矩阵.md`.

Background reading cited above:

- [Compliance with new EU AI Act transparency obligations, Sidley, 2026-09-29](https://sidleycatalyst.sidley.com/)
- [AI vs human code generation report, CodeRabbit, 2025-12-17](https://www.coderabbit.ai/)
- [Five things to avoid when working with AI coding tools, dev.to, 2026-03-12](https://dev.to/)

## Origin of the rule set

The standard was drafted from an assembly of existing writing standards, then
revised through four documented rounds of external review: 12 domain, language,
and region experts; 7 native-speaker reviewers; 10 research-field experts; and
a 26-expert discussion that fixed what a 1.0 release could honestly claim. All
records ship in `references/zh-Hans/`, including the ones that record the
standard contradicting its own rules.

## License

MIT. See [LICENSE](LICENSE).
