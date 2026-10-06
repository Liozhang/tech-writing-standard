# Index of the rule set

English summaries of the operative rules. The authoritative text for the
Simplified Chinese module and the full review record lives in
`zh-Hans/`.

## Version

Version 1.2, dated 2026-10-06. Version 1.2 changed tooling and the index file
only. No rule content changed.

## English summaries

| File | Chinese counterpart | Contents |
|---|---|---|
| 01-charter.md | zh-Hans/02-总纲.md | Scope, five principles, conformance levels, rule format, conflict order, definitions, normative references, governance, conformance assessment |
| 02-generic-rules.md | zh-Hans/03-通用写作规则.md | GEN-001 to GEN-073, language-neutral core rules |
| 03-module-zh-hans.md | zh-Hans/04-语言模块-简体中文.md | ZH-001 to ZH-027 and the localisation parameter table |
| 04-structure-and-delivery.md | zh-Hans/08-结构与交付规范.md | STR-001 to STR-053 |

## Chinese authoritative text

| File | Contents | Status |
|---|---|---|
| zh-Hans/00-索引与定位.md | Master index, revision history, stated limitations | Normative front matter |
| zh-Hans/02-总纲.md | Charter, CON-001 to CON-004, GOV clauses | Normative |
| zh-Hans/03-通用写作规则.md | Generic rules GEN-001 to GEN-073 | Normative |
| zh-Hans/04-语言模块-简体中文.md | Simplified Chinese module ZH-001 to ZH-027 | Normative, reviewed level |
| zh-Hans/05-语言模块-英语.md | English module EN-001 to EN-107, high-safety variant | Normative, reviewed level |
| zh-Hans/06-语言模块-编写指南.md | LANG-001 to LANG-063, module authoring guide | Normative when authoring a module |
| zh-Hans/07-领域扩展.md | DOM-AERO, DOM-MED, DOM-MECH, DOM-SW | Normative within its domain |
| zh-Hans/08-结构与交付规范.md | STR-001 to STR-053 | Normative |
| zh-Hans/09-术语库规范.md | TERM-001 to TERM-040 | Normative |
| zh-Hans/10-工具链与度量规范.md | TOOL-001 to TOOL-072 | Normative |
| zh-Hans/11-标准映射矩阵.md | Rule to source standard mapping, version check record | Informative |
| zh-Hans/01-现有规范汇编.md | Assembly of existing standards, strengths and limits | Informative |
| zh-Hans/12-评审意见汇总.md | Round one, 12 experts | Informative record |
| zh-Hans/13-母语专家复核报告.md | Round two, 7 native speakers | Informative record |
| zh-Hans/14-科研领域评审意见汇总.md | Round three, 10 research-field experts | Informative record |
| zh-Hans/`15-1.0版本建立方案.md` | Round four, 26 experts, what 1.0 may claim | Informative record |
| zh-Hans/16-门禁试跑记录.md | Gate dry-run record, false positive and miss analysis | Informative record |
| zh-Hans/17-端到端符合性演练报告.md | End-to-end conformance drill on two real documents | Informative record |
| zh-Hans/18-完整级关闭记录.md | Disposition of six open items, evidence levels | Informative record |
| zh-Hans/19-真人测试与阈值实测操作手册.md | Protocols for the five human-dependent measurements | Normative, execution class |

## Rule prefixes

| Prefix | Meaning |
|---|---|
| GOV | Charter governance clauses |
| CON | Conformance level clauses |
| GEN | Generic writing rules |
| ZH | Simplified Chinese language module |
| EN | English language module |
| Other languages | Assigned by the two-letter language code, for example JA, KO, AR, HE, DE, FR, RU |
| LANG | Language module authoring guide |
| DOM | Domain extensions |
| STR | Structure and delivery |
| TERM | Termbase |
| TOOL | Toolchain and measurement |

## Levels used in rules

Three levels only. "Must" means non-compliance is non-conformance. "Should"
means comply unless a written reason exists. "May" means recommendation.
Prohibitions are written as "must not". No fourth strength level exists, and
unmapped words such as "shall", "try to", or "suggested" are not used.

## Current open items

Full-level conformance is closed. Five items need real people: human
comprehension testing, screen-reader testing, term project validation,
translation margin measurement, constrained-delivery thresholds. Simulated
readers and language models must not close these gates.
