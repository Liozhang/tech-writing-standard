# 04 Structure and delivery

English summary of `zh-Hans/08-结构与交付规范.md`, STR-001 to STR-053.

## 1. Information structure

STR-001 (must) The structure model is information typing: concept, task,
reference, tutorial, and troubleshooting as the primary model. When DITA is
used, tutorial and troubleshooting map to subtypes of the task class, and the
five-way split is preserved. Source: DITA. Reason: a three-way model does not
cover quick-start and common-problem scenarios in developer documentation.

STR-002 (must) The simplified path of Markdown plus metadata is allowed when
all conditions hold: single language, adapted level, fewer than 200
information units. It must carry information-type labels and unit numbers, and
must be mapped back to the five-way primary model before release. Exceeding one
condition means migration to the full structure. Reason: without a migration
boundary, the two asset types cannot be merged later.

STR-003 (must) Every information unit has a unique number, stable within the
document set, and unchanged when its title changes. Reason: numbers are the
anchor for references, reuse, translation packaging, and change tracking.

STR-004 (must) An information unit must not contain another unit's body text.
Reuse always uses a reference mechanism. The reference syntax is uniform across
the document set, the target must be unique, and circular references are
prohibited. Reason: cycles make content unresolvable and unpublishable.

STR-005 (must) Unit granularity is capped by one unit answering one reader
task or knowledge topic, and floored by "deleting any part damages meaning".
After release, test it with "how many places need changing to change one
thing". More than two means split or switch to a reference. Reason: wrong
granularity raises maintenance cost directly.

STR-006 (should) Heading depth does not exceed three levels. Beyond that, merge
or split the document.

STR-007 (must) Regional differences are handled in two classes. Conditional
differences, such as numbers, units, statements, and plug types, are marked with
conditional attributes inside the unit and published filtered by region.
Content differences, where the step text itself differs, become a separate unit.
Reason: making every difference its own unit duplicates the same operation and
breaks single source of content.

STR-008 (must) Numbering rules for lists, tables, and figures are uniform
across the document set.

## 2. Metadata

STR-010 (must) Every document and information unit carries: unique number,
title, information type, audience, scope, conformance level, applicable language
module and version, module status among guide, draft, reviewed, and full,
applicable domain extension and version, version number, release date,
responsible owner, and status. Status values are draft, under review,
released, and retired. Reason: without module version and status, the object of
certification cannot be determined.

STR-011 (must) Only content with status released may be published. A preview
environment is not a release, and preview content is marked.

STR-012 (must) Research-class documents add a research metadata field group,
conditionally triggered by document type: ethics approval number and body,
informed consent method, trial registration number, grant number, author
contributions in CRediT categories, conflicts of interest, Open Researcher and
Contributor ID, Digital Object Identifier, data and code availability
statement, copyright and licence, and received and revision dates. Missing
items block release. Reason: these fields are the minimum credibility
requirements for research documents.

## 3. Versioning and change

STR-020 (must) Version numbers use one of three schemes and stay uniform
across the document set: three-part semantic version, product version, or
calendar version. With a product version, a mapping table between product
version and content version is maintained.

STR-021 (must) Every release carries change notes naming the affected
information unit numbers and the change type.

STR-022 (must) Changes to safety-related or regulation-related content record
their impact per GEN-071.

STR-023 (must) Content status has six values: released, corrected, expression
of concern, retracted, republished, and retired. Academic corrections follow the
state machine. Corrected means the content has an error, the original version is
kept, and a pointer to the correction note names the corrected unit. Expression
of concern means reliability is in question, the original is kept, and a
prominent notice is added. Retracted means the conclusion is not trustworthy,
the original is kept, a watermark or equivalent notice is applied, and index
holders and downstream citers are notified. Republished means published again
after retraction, with a two-way link to the original. Archived content is
always kept and never physically deleted. Reason: marking everything as retired
flattens the line between a flawed article and an untrustworthy one, which is a
research integrity defect.

STR-024 (must) Source files are under version control, and every change traces
to a responsible person and a review record. Source: ISO/IEC/IEEE 26511.

STR-025 (must) Multilingual synchronisation deadlines are registered in project
documents. While translation lags, the source-language release marks the units
not yet covered, and units in translation are locked in terminology and
structure. Do not revise while translating. Reason: an unlimited synchronisation
window guarantees permanent multilingual drift.

## 4. Release

STR-030 (must) The same content supports multiple formats. A printable version
outputs a tagged Portable Document Format file or provides an equivalent web
path. Reason: an untagged Portable Document Format file is inaccessible to
screen readers.

STR-031 (must) Multilingual versions share the information unit structure and
swap only language variants. A structure change is synchronised across all
language versions.

STR-032 (must) Translation packages are handed over per the LANG-050 handover
package specification.

STR-033 (must) The release pipeline runs the must-level gates from the toolchain
rules. Content that does not pass is not released. Preview and draft
environments may run only the metadata and link checks among the must items.

STR-034 (must) Public-facing web documentation meets WCAG level AA.

## 5. Accessibility

STR-040 (must) Documents mark the page language and fragment language
attributes, so screen readers can switch voices in multilingual text. Source:
WCAG language attribute requirement. Reason: missing language attributes make
mixed content read as noise, the most serious localised usability defect.

STR-041 (must) Text contrast is 4.5:1 for body text, 3:1 for text at 18 point
or 14 point bold and above, and 3:1 for icon and control borders. Source: WCAG
level AA values. Reason: no numbers means no check.

STR-042 (must) Pages scale to 400 percent or a viewport width of 320 pixels
without loss of content or function, verified on the release template. Source:
WCAG reflow requirement.

STR-043 (must) Right-to-left versions are typeset separately and proofread, not
mirrored and left alone. The proofreading checklist covers punctuation, table
column order, figure direction, form and input control direction, navigation,
menu expansion direction, scrollbar direction, binding direction, table of
contents page number direction, bookmark and navigation order, and mobile
screenshots. The checklist maps item by item to the TOOL-021 checks. Metadata
records the native-speaker reviewer. Reason: a single missing item leaves its
defect unblocked at the gate.

STR-044 (must) Time-based media, meaning video, audio, and animation, provide
captions or a transcript. Source: WCAG.

STR-045 (must) Content is keyboard operable, and focus order matches reading
order. Source: WCAG.

STR-046 (must) Complex tables with multi-level headers are decomposed or given
an equivalent structure. Row and column limits are set in the template.
Source: WCAG.

STR-047 (must) Non-text content contrast reaches 3:1. Source: WCAG.

## 6. Resource-constrained delivery

STR-050 (must) Alternative delivery forms are defined for low literacy, low
bandwidth, offline, and no-power scenarios: monochrome print contrast
thresholds and minimum stroke width, image size ceilings for low bandwidth,
offline single-file specification, and self-containment requirements for paper
documents without power. Specific values are filled in by the organisation per
target market. A domain extension that has not filled them in must not claim
coverage of that market. Source: this standard's added principle five. Reason:
corresponds to principle five.

STR-051 (must) A figure-only version is provided per GEN-064, with figure steps
corresponding one to one with text steps. Before release, sample-verify that
the figures are understandable, using the same acceptance method as
comprehension testing.

STR-052 (must) Translation length margin comes from the language module
parameter table and is compared on both character count and rendered width.
Templates must not use fixed-height containers, fixed line counts, or absolute
positioning. String ceilings and truncation strategy are defined. Languages
whose compounds cannot be broken apply the module's hyphenation and truncation
rules. Before release, compare finished lengths against the margin. Reason:
reserving space without checking equals not reserving it, and a word-count ratio
underestimates expansion.

STR-053 (must) Documents for the European Union declare the member states of
sale and their official language version list, and cover the regulation-required
companion content: declaration of conformity reference, authorised
representative in the Union, waste electrical and electronic equipment recovery
and separate collection instructions with symbols, and EN 301 549 where the
European Accessibility Act applies. Source: Regulation (EU) 2023/1230 on
machinery, Regulation (EU) 2023/988 on general product safety, the waste
electrical and electronic equipment directive, and the European Accessibility
Act. Reason: the Union's language and legal content requirements are acceptance
items, not options.
