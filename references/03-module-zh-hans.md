# 03 Simplified Chinese language module (zh-Hans)

English summary of `zh-Hans/04-语言模块-简体中文.md`, ZH-001 to ZH-027. The
Chinese text is authoritative. This module is at reviewed level: expert review
is done and machine gates cover the machine-checkable items, but real-reader
comprehension testing and limit measurement are not done, so the numbers below
must not be used for full-level acceptance.

## 1. Language basis

ZH-001 (must) Use standard modern written Mandarin. Do not use dialect words,
internet slang, or trade jargon.

ZH-002 (must) Do not invent words. A new concept enters the document only after
the termbase approves it.

ZH-003 (must) Abbreviations follow GEN-042. Abbreviations of proper nouns
already fully generic in Chinese, such as API and HTML, keep their original
form with the meaning stated. All others give the full form at first
occurrence.

ZH-004 (should) One concept uses one form within the document set. Do not swap
synonyms for variety.

## 2. Sentence form and length

ZH-010 (must) Sentence length is measured in characters, not words. The
descriptive limit is 50 characters with a hard ceiling of 65. Operation steps
use a tighter limit, set in the parameter table. Safety-critical documents use
25 characters for operations. Exceeding the regular limit requires a rewrite.
Exceeding the hard ceiling blocks release.

Counting rules:

- Sentence boundaries are the full stop, question mark, and exclamation mark.
  The enumeration comma does not end a sentence. Semicolon-linked parallel
  clauses are counted separately, and the longest clause decides.
- Punctuation is not counted.
- Each Chinese character counts as one.
- A continuous digit string, such as a date, model number, or parameter value,
  counts as one token.
- Continuous Latin text is split on spaces, and each word counts as one.
- Terms, identifiers, and code units are not counted.

The current limits come from a percentile measurement on a 326-sentence corpus
plus native-speaker review: operations 90th percentile 42 characters, 95th
percentile 46; descriptive 90th percentile 50, 95th percentile 65. Steps four
and five of the limit determination, real-reader comprehension testing and
signature, are not done. Reason: a word-count method does not apply to a
language without spaces between words.

ZH-011 (must) One sentence carries one meaning. Do not use three or more levels
of modification. Split a sentence when its attributive is too long. Reason:
long attributive chains are the main source of Europeanised Chinese.

ZH-012 (should) Write operation steps as imperative short sentences naming the
action directly. Use "please" sparingly.

ZH-013 (should) Use the active voice where it is clear. Use the passive for
uncontrollable system events, for example a state being overwritten or a
signal being reset. Reason: the passive is more accurate there.

ZH-014 (must) Two negation words must not appear consecutively in one
sentence.

ZH-015 (should) One paragraph carries one topic. A paragraph has at most six
sentences. Use a list when content gets complex. This is an experience value
and may be adjusted by review.

## 3. Punctuation

ZH-020 (must) Punctuation follows GB/T 15834.

ZH-021 (must) Quotation marks and brackets follow the national standard. Two
levels of quotes are used consistently throughout. Bracket nesting follows the
standard order. Title marks are limited to standard names, work names, and
article names. File names, button names, menu names, and parameter names do not
use title marks. Reason: title-mark abuse is a frequent error in Chinese
software documentation.

ZH-022 (must) The three connecting marks divide their work per GB/T 15834: the
wave dash for numeric ranges, the one-em dash for spans, the hyphen for
compounds. Ellipsis is six dots. The dash is two em. Headings take no
sentence-final punctuation.

ZH-023 (must) In mixed Chinese and Latin text, put one space between a Chinese
character and a Latin letter or digit. Do not add or remove spaces around
full-width punctuation. Established mixed forms are exempt, including product
names and model numbers, source labels, and forms registered in the termbase as
do-not-translate. Exempt forms must be registered in the termbase, and
unregistered forms follow this rule. Reason: mixed-script spacing is the most
frequent visual defect in Chinese technical documents, but forcing spaces into
customary product names hurts search and recognition.

ZH-024 (must) Chinese sentences use full-width punctuation. Symbols inside
technical expressions, code, version numbers, and model numbers stay
half-width. Thousands separators inside numbers use the half-width comma, and
numbers below five digits are not grouped.

ZH-025 (must) Interface elements and code objects have one consistent form:
buttons, menu items, and tabs are marked with quotation marks. Command lines,
parameter names, function names, paths, and error codes use code format. The
same object uses one form throughout.

ZH-026 (should) List items generally take no sentence-final punctuation. If list
items are full sentences, add full stops consistently. Parallel words are
separated by the enumeration comma, parallel clauses by the semicolon.

ZH-027 (must) Sentence length follows ZH-010. Semicolon-linked parallel clauses
are counted separately, and no enumeration exemption exists. Rule-definition
sentences, which start with a rule number, are the only relaxed class and stay
under 100 characters, because they carry fixed components of number, level,
source, and reason. Informative annexes 01 and 12 to 18 are exempt from the
length limits, because preserving review intent takes priority there. Reason:
relaxing on a semicolon would allow selective application.

## 4. Numbers, dates, and units

ZH-030 (must) Numbers follow GB/T 15835. Statistics, physical quantities,
identifiers, and dates use Arabic numerals. Idioms, approximate quantities, and
rhetorical expressions use Chinese numerals. Do not stack an Arabic numeral
with an approximate word.

ZH-031 (must) Dates follow GEN-050. The registered authoritative calendar is
Gregorian, and it is the sole authority. For readers in China, the Chinese form
may be given alongside, with the ISO 8601 numeric form as the interpretation
object.

ZH-032 (must) Units use the International System of Units. Unit names are in
Chinese, symbols follow the national and international convention, and one
space separates a value from a unit symbol.

## 5. Terms, personal names, and place names

ZH-040 (must) Scientific and technical terms prefer the forms published by the
China National Committee for Terms in Sciences and Technologies. Unlisted terms
go through the termbase process.

ZH-041 (must) Foreign personal and place names follow the customary
translation, with the original given at first occurrence. Keep the original
where no customary translation exists.

ZH-042 (should) Romanisation of Chinese names and places follows GB/T 16159.

## 6. Accessibility and read-aloud

ZH-050 (must) The document provides a text layer that can be read aloud.
Scanned images do not count as body text.

ZH-051 (should) Long documents provide a table of contents and an index.
Directory entries match the chapter titles character for character.

## 7. Localisation parameter table

| Parameter | Value |
|---|---|
| Length unit | Character, counting rules in ZH-010 |
| Operation sentence limit | 35 characters |
| Descriptive sentence limit | 50 characters |
| Text direction | Left to right |
| Vertical layout | Not supported |
| Interword spaces | None. One space between Chinese and Latin text |
| Date format | 2026-10-06, optionally alongside 2026 年 10 月 6 日, with the numeric form as interpretation object |
| Authoritative calendar | Gregorian |
| Calendar authority order | Gregorian only |
| Time format | 24-hour, HH:MM, with HH:MM:SS where needed |
| Thousands separator | Half-width comma, no grouping below five digits |
| Decimal point | Half-width full stop |
| Currency format | Symbol first, for example ¥100.00 |
| Unit naming | Chinese full name plus international symbol |
| Numeric system | Arabic numerals |
| Calendar | Gregorian |
| Name order | Family name first |
| Address order | Province, city, district, street address, recipient |
| Telephone format | International form +86-xxx-xxxx-xxxx |
| Collation | Pinyin order |
| Politeness level | Address the reader as 您, keep honorifics minimal |
| Honorific and plain forms | Not applicable |
| Phonetic annotation | Not applicable |
| Chinese character ratio ceiling | Not applicable |
| Naming authority | China National Committee for Terms in Sciences and Technologies |
| Translation length margin | To be measured and filled in. Not usable for full level until filled |

**Note on a live discrepancy.** ZH-010 in the Chinese text sets the operation
limit at 40 characters with a hard ceiling of 45, while the parameter table
above registers 35 characters. The Chinese module has not resolved this. Until
it does, keep operation sentences at or below 35 characters, which satisfies
both readings. Recorded here rather than silently harmonised.
