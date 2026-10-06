# 02 Generic writing rules

English summary of `zh-Hans/03-通用写作规则.md`, GEN-001 to GEN-073. These
rules are language-neutral. Sentence length, punctuation, and number format
belong to the language module, not here. Examples in the Chinese text explain
and do not constrain.

## 1. Document positioning

GEN-001 (must) Each document serves one reader task set and is organised by the
reader's task, not by internal system or department boundaries. Source:
ISO 24495-1 principle one. Reason: readers search by goal and do not care about
internal structure.

GEN-002 (must) Each document states its audience, scope, version number, and
release date. All four are mandatory. Reason: unclear audience is the main
cause of documents that lead to wrong actions.

GEN-003 (should) Each document opens with a summary of at most one tenth of its
length. Source: ISO 24495-1 principle two.

## 2. Information types

GEN-010 (must) Content is organised into five information units: concept,
task, reference, tutorial, troubleshooting. Each unit is labelled with its
type. Source: DITA model extended with the common four-way practice. Reason:
mixed types are the main cause of readers misusing operational content.

GEN-011 (must) Concept units answer "what is it and why". Task units answer
"how to do it", one step per action. Reference units supply lookup data.
Tutorial units follow a learning path for first-time users. Troubleshooting
units are organised by symptom and give a decision procedure. The five types
must not be mixed. Reason: type mixing is the main cause of reader misuse.

GEN-012 (must) Information units are independently referenceable, their titles
summarise the content, and their numbers are stable within the document set.
Reason: this supports single-point editing, reuse, and split translation.

## 3. Safety warnings

GEN-020 (must) Safety warnings have four levels: danger, warning, caution,
notice. Danger means death or serious injury will follow if not avoided.
Warning means death or serious injury can follow. Caution means minor injury or
equipment damage can follow. Notice means information required for correct
operation. Level definitions are uniform across the document set. Source:
IEC/IEEE 82079-1, with the fourth level taken from aerospace practice. Reason:
without the notice level, non-risk explanations get listed as risk levels and
the risk signal is diluted.

GEN-021 (must) A safety warning sits before the step it applies to. Source:
IEC/IEEE 82079-1. Reason: by the time the reader reaches the step, the harm has
happened.

GEN-022 (must) A safety warning opens with a command or a condition: what to do
or what condition must hold, and only then the consequence of not doing it.
Source: ASD-STE100 warning rules, IEC/IEEE 82079-1. Reason: leading with the
consequence delivers risk information before the reader has understood the
action, which weakens the warning.

GEN-023 (must) The fixed warning form has four parts: signal word, hazard,
consequence, countermeasure. Source: IEC/IEEE 82079-1 sentence convention.
Reason: only a complete form supports compliance evidence.

GEN-024 (must) A safety warning must not share a visual block with promotional
or encouraging content. Reason: that weakens the seriousness of the warning.

GEN-025 (must) The same risk reuses the same warning wording across documents.
Warning wording is managed in the termbase. Reason: inconsistent wording is
read as a different risk.

GEN-026 (must) Operations involving energy isolation must define a lock-out
tag-out procedure: cut the energy source, apply locks, hang tags, verify zero
energy, work, then release in reverse order. Multi-person work defines each
person's lock and the mutual confirmation. Source: mechanical industry safety
practice. Reason: energy isolation failure is the highest-frequency mechanical
accident stage.

## 4. Procedure steps

GEN-030 (must) One step contains one action unit. The language module defines
the action unit and registers indivisible compound actions, such as
press-and-hold, as exceptions. This standard does not define a grammatical test
for an action unit. Reason: multi-action steps are the leading cause of missed
operations, and action units are expressed differently in each language, so
the generic layer cannot define the test.

GEN-031 (must) Conditions come first: state the condition, then the action. The
form is "when condition X holds, do action Y". Reason: a trailing condition
makes the reader act first and discover the precondition afterwards.

GEN-032 (must) The first step of every procedure is an immediately executable
entry action. Do not open with background. Reason: the reader came to act.

GEN-033 (must) Steps are numbered consecutively with no gaps and no repeats.
References to steps use the number. Reason: this supports verbal handover and
remote support.

GEN-034 (must) Key operations give a completion criterion. The criterion must
include a visual or textual basis and must not rely on hearing or touch alone.
Source: WCAG sensory characteristic requirement. Reason: single-sensory
criteria fail for readers with disabilities.

GEN-035 (should) Reversible and irreversible operations are stated separately.
An irreversible step gives a confirmation method before it.

GEN-036 (must) Do not use logical double negation for operational
requirements. The grammatical negation of a language does not count as logical
double negation, and the language module states which cases are exempt.
Reason: logical double negation is widely misunderstood, and a literal rule
would wrongly hit languages with agreement negation.

GEN-037 (should) Recovery and exception handling form their own section and are
not mixed into normal steps.

## 5. Language expression

GEN-040 (must) One sentence carries one meaning. Do not use three or more
levels of modification. Reason: long modification chains are the main cause of
comprehension failure.

GEN-041 (must) Terminology is consistent throughout. One concept uses one word.
Synonym mixing is prohibited.

GEN-042 (must) An abbreviation is given in full with its meaning at first
occurrence. The short form may be used afterwards. Commands, identifiers, error
codes, and abbreviations inside code examples are exempt. Reason: undefined
abbreviations are the highest-frequency barrier in multilingual documents.

GEN-043 (must) Every pronoun and demonstrative must refer back without
ambiguity. Do not refer across long distances. Reason: referential ambiguity is
amplified in translation.

GEN-044 (must) The actor and the object of an action must be determinable
without guessing. Whether a language may drop the subject, and how
determinability is kept when it is dropped, is defined by the language module.
The boundary for generic subjects such as the French "on" is also set by the
module. Reason: an undeterminable actor or object leaves the reader guessing.

GEN-045 (should) Use the person, register, and politeness level the language
module specifies, and speak directly to the reader. Where a language has no
stable second person, the module's polite form achieves the same effect, and
unnatural second-person pronouns must not be forced in. Source: ISO 24495-1
principle three. Reason: instructions addressed to the reader are followed more
often, and politeness is a language question.

GEN-046 (must) Do not use slang, puns, humour, or culture-specific allusions.
Test: any expression that needs specific cultural background, cannot be
registered in the termbase, or loses meaning in literal translation is not
used. Reason: these do not translate and are understood inconsistently across
regions.

GEN-047 (must) Do not use wording that discriminates by gender, region,
ethnicity, or disability.

GEN-048 (should) Prefer cross-culturally universal graphical symbols for
operations, and manage symbol entries in the termbase.

## 6. Region and localisation

GEN-050 (must) Dates: the authoritative calendar is registered by the language
module. Gregorian dates default to the ISO 8601 numeric form, authoritative
calendar dates are given alongside as the module requires, and the
interpretation object is stated. ISO 8601 covers the Gregorian calendar only
and must not be forced on regions where another calendar is authoritative.
Reason: the numeric form is unambiguous worldwide, and calendar authority is a
regional decision.

GEN-051 (must) Measurement units use the International System of Units. Where
an industry unit is customary, give the conversion at first occurrence.
Industry-specific units are registered by the language module. Reason: mixed
units are a cause of cross-border documentation incidents.

GEN-052 (must) Amounts, addresses, and telephone numbers use parameter
placeholders, with the format filled in per region by the language module.
Reason: this keeps one region's format out of the core.

GEN-053 (must) Figures keep an extractable text layer. Text inside a figure
enters the translation package and is checked against the termbase. Text that
the body text needs must not be rendered as an unextractable bitmap. Source:
DITA figure-text separation practice. Reason: figure text that cannot be
localised is the most common source of rework.

GEN-054 (must) Layout reserves space for translation length change, both
expansion and contraction. The ratio comes from the module's measured value.
Reason: fixed-size boxes overflow or leave gaps after localisation.

GEN-055 (must) Code blocks, inline code, commands, paths, and configuration
file content are not subject to the module's punctuation, sentence, and
spelling rules. The orientation, line numbering, and line breaking of
local-language comments inside a code block are defined by the module. Reason:
rewriting code characters breaks execution, and right-to-left languages need a
separate rule for comment direction.

## 7. Figures and tables

GEN-060 (must) Every figure has a number and a caption. For operational
figures, the step numbers in the figure correspond one to one with the step
numbers in the text. Reason: without correspondence, figure and text cannot
cross-check each other.

GEN-061 (must) Figures have alternative text. Decorative figures are marked
with empty alternative text. Source: WCAG. Reason: unmarked decorative figures
make screen readers read noise.

GEN-062 (must) Tables have header rows, one record per row. Do not use tables
for layout. Reason: layout tables break reading order for assistive
technology.

GEN-063 (must) Colour must not be the only carrier of information. Source:
WCAG.

GEN-064 (should) Provide a figure-only version for low-literacy readers, with
figure steps corresponding one to one with text steps. Release and acceptance
follow the structure and delivery rules.

GEN-065 (must) At first occurrence of an interface symbol or icon, state its
shape, its location, or the result of activating it. Do not assume the reader
knows the symbol. Source: target-reader retesting, where low-literacy readers
stalled at unfamiliar symbols. Reason: an unknown symbol stops the reader, and
a short sentence does not help.

GEN-066 (should) For public-facing documents, attach one plain-language
explanation at a term's first occurrence, and do not introduce a new term
inside that explanation. Source: target-reader retesting, where ordinary
readers did not understand "origin" and low-literacy readers skipped sentences
containing "default" and "compute". Reason: terminology is the leading cause of
comprehension failure for public documents, and explanation sentences cost
little.

GEN-067 (should) For public-facing documents, parentheses and dashes must not
carry required information. Required information is written as a body step.
Source: target-reader retesting, where low-literacy readers skipped all
parenthetical and dashed content. Reason: content readers skip cannot be a key
step.

## 8. Maintainability

GEN-070 (must) The document set uses a termbase. Entries are keyed on concept.
Graphical symbols are managed as entries too.

GEN-071 (must) Changes to safety-related or regulation-related content record
their impact and flag it to readers in the version notes. Reason: silent change
of safety information is extremely risky.

GEN-072 (should) Provide a reader feedback channel, and route feedback into the
measurement loop.

GEN-073 (must) Identical content is maintained in one place and referenced
elsewhere. Do not copy. Reason: copying is the root of multilingual version
drift.
