# 01 Charter

English summary of `zh-Hans/02-总纲.md`. Rule numbers match the Chinese text.
Where the two disagree, the Chinese text is authoritative and the disagreement
is a defect to report.

## 1. Purpose

The standard gives product technical documentation a single basis for writing
and publication, so that a document achieves five outcomes. The reader gets the
needed content, finds it quickly, understands it correctly, knows how to use
it, and can still get and use it when resources are constrained. The long-term
goal covers more industries, more languages, and more regions. The current
scope is set by section 2 below. Anything outside that scope must not be used
as a basis for a conformance claim.

## 2. Scope

Applies to:

- Document types: product manuals, software documentation, operations
  runbooks, user guides, training material.
- Languages: Simplified Chinese and English, the two languages with a reviewed
  module. Other languages have only a module-writing guide and a parameter
  table, and must not support any conformance claim.

Does not apply to:

- Publication-oriented research writing: journal papers, theses, preprints,
  systematic reviews, study protocols, data management plans, grant
  applications. These follow the applicable national standards and the rules of
  the target journal or academic community. A research extension is on the
  roadmap and is not yet released.
- Creative writing, marketing copy, formal legal text.

For documents touching safety, conformity assessment, or administrative
approval, the law, regulation, and product standards of the applicable region
come first. This standard governs the writing layer and does not replace
registration documents. Domain extensions add writing-layer content only and
are not proof of product compliance. Adopters must check current regulation for
their target market.

## 3. Principles

The first four are taken from ISO 24495-1:2023. The fifth is added by this
standard. No rule may violate these principles. When principles conflict, the
one with the largest effect on reader safety and comprehension wins.

1. Relevant content. Document only what the reader needs to finish the task.
2. Findable. The reader reaches the target information within three steps.
3. Understandable. Language, sentence form, terminology, and figures match the
   comprehension of the target reader group.
4. Usable. After reading, the reader knows what to do and can confirm it was
   done correctly.
5. Resource-constrained adaptation. The reader may lack literacy, reliable
   network, or stable power. The document must provide graphical, spoken, and
   offline alternatives.

## 4. Conformance levels

- Full level. All must-level rules plus domain extensions, with human
  comprehension testing, screen-reader testing, and two-person review. For
  safety-critical and regulated documents.
- Reviewed level. All must-level rules. Should-level items may be waived by
  review. For general product documents.
- Adapted level. All must-level rules. May-level items are optional. For
  general-audience content.

CON-001 (must, all documents) Regulated documents, and documents whose domain
extension sets a floor, must take the full level. The level is declared by the
document owner in the metadata and cannot be lowered afterwards. Level choice
enters the quality record. Reason: a low level must not be used to dodge
regulation.

CON-002 (must, maintenance group) A domain extension may set a level floor for
its domain. When several extensions apply, take the highest floor.

CON-003 (must, all documents) Safety-related rules accept no level waiver.
Reason: safety content never degrades with document level.

CON-004 (must, all documents) Module status has four grades. Guide level means
only a module-writing guide and a parameter table exist. Draft level means the
module is written but not reviewed by experts. Reviewed level means domain and
native-speaker review is done, machine gates cover the machine-checkable items,
and human comprehension testing and limit measurement are not done. Full level
means real-reader comprehension testing passes and a limit-determination record
is registered. Reviewed and draft modules must not be used for full-level
documents. Guide and draft modules must not be used for reviewed-level
documents. Each module's registration carries its status and a list of open
items, where an open item is evidence the module does not yet have. Reason:
results of unreviewed rules cannot be judged, and status grades must match the
actual evidence type, with no rating inflation.

## 5. How rules are written

Every rule has five elements: number, level, scope, source, and reason. All
five are mandatory. Levels use only must, should, and may. Scope names the
object the rule acts on. Source names the authority the rule comes from, and
self-defined rules state "self-defined" plus the basis. Reason is one sentence
naming the problem the rule solves.

## 6. Conflict order

When rules conflict, the first applicable in this order wins:

1. Law, regulation, and mandatory standards of the applicable region.
2. The contract and the customer specification it cites.
3. Writing rules issued by the target journal, academic community, or industry
   body.
4. Mandatory industry requirements in domain extensions.
5. Language module rules.
6. Generic rules.
7. Principles.

GOV-010 (must, all documents) Deviating from this order requires a written
deviation process with five elements: applicant, deviation scope, reason,
compensating measure, and approver. It is valid only when all five are present
and it is registered. Reason: an unapproved deviation abandons conformance.

## 7. Multilingual and multi-region principles

- Language neutrality. Generic rules must not contain formulations valid for
  one language only. Rules about sentence form, punctuation, and format belong
  in the language module. Examples in generic rules explain, they do not
  constrain.
- Regional parameterisation. Dates, numbers, units, currency, addresses,
  telephone numbers, and collation are always parameters, filled in per region
  by the language module.
- Single core. Language modules and domain extensions only add. They must not
  modify generic rules. When a change is needed, it goes through the change
  process.
- Testing. Before each language version is released, run comprehension testing
  per the toolchain rules.

## 8. Terms and definitions

Information unit: the smallest content unit that can be numbered, released, and
translated on its own, mapping to one reader task or one knowledge topic.
Concept: the unique designation of an object or abstraction, the primary key of
the termbase. One concept may have forms in many languages. Termbase: a
database keyed on concept that manages multilingual forms and their status.
Language module: all the concrete writing rules and localisation parameters for
one language. Domain extension: a rule set adding mandatory requirements for one
industry. Conformance level: the strictness a document declares it follows.
Comprehension test: an acceptance method where target readers summarise key
points or demonstrate a procedure after reading. Single source of content: one
content item is maintained in one place and referenced elsewhere. Action unit:
one indivisible operation in a step, judged by the language module. Parameter
tables of actions count as one unit. Limit-determination record: the archive of
how a language module's sentence limit was set, with corpus, percentiles,
native-speaker review, comprehension test conclusion, and signatures. Module
status: the four-grade maturity scale defined by CON-004. Term baseline: the set
of forms exported from the termbase for writing and translation, including the
banned-form list and the do-not-translate list.

## 9. Normative references

ISO 24495-1, IEC/IEEE 82079-1, ASD-STE100, ISO 8601, the International System
of Units and IEC 80000 series, ISO 15223-1, ISO 13485, ISO 12100, ISO 17100,
ISO 30042, OASIS DITA, W3C WCAG, GB/T 1.1, GB/T 15834, GB/T 15835, GB/T 16159.
References are undated, so the latest edition applies. Verifying the edition is
the maintenance group's duty, not the adopter's.

Informative only: GB/T 7713 series and GB/T 7714. They apply to research
writing, which this standard does not cover.

## 10. Governance and versions

The model is one core plus many modules. The charter and generic rules are
managed by the maintenance group. Language modules are maintained by
native-speaker experts. Domain extensions are maintained by industry
representatives. Language modules and domain extensions carry their own version
numbers, and their updates do not trigger a renumbering of the whole standard.
A review happens every twelve months, with a conclusion of confirm, revise, or
withdraw. When a parent standard is reissued, the comparison revision is done
within three months and registered in the mapping matrix. An organisation may
cut a subset, but must not claim conformance and then modify a must-level rule.

## 11. Conformance assessment

Assessment samples the document set. Full level is assessed document by
document. Reviewed level is assessed at ten percent per batch. Adapted level is
sampled at the release node. Non-conformities fall into three classes. Blocking
items are must-level failures and stop release. Remediation items are
should-level failures and get a deadline. Observation items are may-level
failures and are recorded. Waivers apply to should-level items only, need
written approval, and are registered. Must-level items cannot be waived. Waiver
records, sampling records, and test records are archived with the document set
for at least the document's lifetime plus two years.
