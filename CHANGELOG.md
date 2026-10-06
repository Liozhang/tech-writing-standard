# Changelog

All versions, in reverse order. A version that changes only tooling says so.

## 1.2 — 2026-10-06

Tooling and index only. No rule content changed.

- Gate script directory collection became recursive and skips hidden
  directories, so documents nested in subdirectories are no longer missed.
- Termbase path is now resolved from the script location, so the script runs
  from any working directory.
- Added an optional `--termbase <path>` argument so an organisation can check
  against its own termbase. The parser was refactored into a testable function.
- Unit tests grew from 24 to 26. Recursive collection and the termbase argument
  each have a test.
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
