# Changelog

All versions, in reverse order. A version that changes only tooling says so.

## 1.2.1 — 2026-10-06

Skill metadata only. No rule content changed.

- The skill description in `SKILL.md` was 1277 characters. The Agent Skills
  specification, which Claude Code enforces, caps the description at 1024
  characters. The skill installed in ZCode but would not have been accepted by
  a client that validates the limit. The description is now 962 characters and
  keeps every trigger phrase.
- Both READMEs gained a two-platform install table covering ZCode and Claude
  Code, user and project scope, with the two compatibility facts that make the
  install work: the name matches the directory and uses only the allowed
  characters, and the description is inside the limit.
- Version bumped to 1.2.1 rather than folding the fix into 1.2, because v1.2 is
  already released and a released tag should not move.

## 1.2 — 2026-10-06

Tooling, index, and presentation only. No rule content changed.

- Gate script directory collection became recursive and skips hidden
  directories, so documents nested in subdirectories are no longer missed.
- Termbase path is now resolved from the script location, so the script runs
  from any working directory.
- Added an optional `--termbase <path>` argument so an organisation can check
  against its own termbase. The parser was refactored into a testable function.
- Fixed a gap in the gate scripts against TOOL-020. Markdown image and link
  addresses were not masked, so the percent-encoded fragments inside a badge
  URL were counted as English words and markdown links broke sentence counts.
  The mask keeps the alternative text and the link text, and drops the
  address. Documented because it is a defect the standard required and the
  scripts had not delivered.
- Unit tests grew from 26 to 27. The address mask has a test, and that test
  includes a reverse case proving real English sentences are still caught.
- Both READMEs gained badges and repository metadata: a description naming the
  rule count, the modules, the extensions, the termbase, the gates, and the
  standards, plus twelve topics for discoverability. Badges were re-checked
  through all four gates after being added.
- The index file was itself revised under the standard: six sentences over the
  50-character descriptive limit, one over the 100-character hard ceiling, and
  two mixed-script spacing misses were fixed. Table rows are counted as layout,
  not as violations.
- Bilingual repository layout introduced: English primary entry point plus a
  Chinese entry point, English rule summaries in `references/`, authoritative
  Chinese text and the full review record in `references/zh-Hans/`.
- A recorded discrepancy was left in place rather than silently harmonised:
  ZH-010 sets the operation sentence limit at 40 characters, while the Chinese
  module parameter table registers 35. Operation sentences must stay at or
  below 35 until the module resolves it. See
  `references/03-module-zh-hans.md`.

## 1.1 — 2026-10-06

- `doccheck.py` gained English, accessibility, and term gate modes.
- Unit tests grew to 24.
- A demo termbase was created and the three terminology gates were walked end
  to end.
- Translation length margin was measured on five Chinese-English pairs: ratio
  4.20 with a range of 3.41 to 5.48. Recorded as a reference interval, not a
  certified value.
- Paired-version comprehension testing with simulated readers hit a ceiling
  effect and was recorded as insufficient evidence. This is why full level
  stayed closed.
- A substring false positive in the term gate was fixed, with a regression
  test.

## 1.0 — 2026-10-06

First formal release. Scope was deliberately narrowed to what had been
verified. The end-to-end conformance drill on two real documents closed three
governance gates. Five items were listed as open rather than claimed.

## 0.1 to 0.7 — 2026-10-06

Draft series. Notable points: external review by 12 experts, 7 native speakers,
and 10 research-field experts. Version 0.5 found the standard violating its own
sentence-length rule in 99 places, and the normative body was rewritten until
all four gates reached zero. Version 0.6 separated table rows and
machine-generated long lines from body-text sentence counting, after tests
showed they are layout, not violations.
