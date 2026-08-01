# tools/

## tic_scanner.py

A command-line tool that flags candidate AI-writing tics in a markdown draft. Built for this project's essay-editing workflow, but the core approach (word-boundary regex + heuristic classification, no ML, no API calls) is generic enough to point at any prose.

### Requirements

Python 3, standard library only — no dependencies to install.

### Usage

```
python tic_scanner.py path/to/essay.md
python tic_scanner.py path/to/essay.md --threshold-words 35
python tic_scanner.py path/to/essay.md --context-chars 80
```

- `--threshold-words` (default 35) — sentence length, in words, to flag as a run-on.
- `--context-chars` (default 50) — characters of surrounding context to show around each hit.

### What it checks

1. **Em-dash density** — flags overuse (>8 per 1,000 words), and breaks the count down two further ways:
   - **Weak "— and" / "— but" clause-joins** — the single clearest formulaic tell found across every essay this tool was built on: two independent clauses stitched together with a dash where a period or comma reads more cleanly.
   - **Dash structure by sentence** — classifies each sentence's dash count. Two dashes in one sentence usually means a genuine bracketing pair (a mid-sentence parenthetical, worth keeping). One dash usually means a single-sided appositive or clause-join that a colon or period could replace just as well. Three or more is irregular and gets flagged for a manual read rather than a guess.
2. **Inflated vocabulary** — a curated list (delve, tapestry, robust, leverage, synergy, intrinsic, culmination, and about 60 more) of words that show up disproportionately in LLM output relative to ordinary prose. Partly merged from [FareedKhan-dev/Detect-AI-text-Easily](https://github.com/FareedKhan-dev/Detect-AI-text-Easily)'s word list, trimmed of entries too common in normal writing to carry real signal (core, facet, unity, harmony) and a couple that read as dataset noise in the source ("Digital Bazaar", "Catering").
3. **Hedging / meta-commentary** — phrases that gesture at a claim's significance instead of asserting it ("it's worth noting," "worth sitting with," "arguably," "at the end of the day").
4. **"Not just X, it's Y"** — the single most recognizable LLM sentence formula.
5. **Frozen verbs (nominalizations)** — "make a decision" instead of "decide," "conduct an analysis" instead of "analyze."
6. **Long sentences** — length as a rough run-on proxy, not a hard rule.

### Design philosophy

This is a heuristic flagging tool, not a judge. It finds candidates; a human decides whether each one is doing real work (keep) or padding (cut). False positives are expected and acceptable — silently missing something is the worse failure. Every category is a plain word-boundary regex or substring match against a curated list; there's no scoring, no weighting, no verdict.

### Adapting it to another project

Two pieces of this scanner are tuned specifically to this project's conventions, and should be reconsidered before pointing it at a different codebase:

- `CITATION_LINE` assumes footnote/reference lines start with a superscript numeral after a dash (`- ¹`, `- ²`, ...) — this project's citation format. Adjust the regex, or remove the exclusion, if your source material cites differently.
- `REVISION_LOG_HEADING` strips everything from a `## Revision log` heading onward, since this project appends dated development notes to the bottom of every essay file and those notes would otherwise get scanned as if they were the prose itself. Rename or remove this if your files don't have an equivalent trailing metadata section — otherwise the tool will happily scan your entire file with nothing stripped, which is harmless but pointless.

Everything else — `INFLATED_VOCAB`, `HEDGING_PHRASES`, `FROZEN_VERBS`, `WEAK_DASH_PATTERN`, the long-sentence threshold — is plain data at the top of the file, meant to be edited directly rather than configured externally.

### Known limitations

- The sentence splitter is a crude regex (`re.split` on `.!?` followed by whitespace) — it doesn't understand markdown headings, blockquotes, or citation-link markup that sits directly after a period with no following whitespace. On files with those, it can occasionally glue two unrelated chunks together into one inflated "sentence," most visibly in the long-sentence category. Harmless in practice — the wrong-looking hits are easy to recognize and dismiss on read — but worth knowing about rather than trusting blindly.
- No detection of quoted material. A word or phrase inside a direct quote from someone else gets flagged exactly the same as the essay author's own prose (a real false positive seen in testing: OpenAI's own "state-of-the-art" phrasing, quoted in an essay, got flagged as the essay's inflated vocabulary).
- English only, and the word/phrase lists reflect current (2026) LLM output patterns — they'll drift out of date as models change.
