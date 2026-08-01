#!/usr/bin/env python3
"""
tic_scanner.py — flags common AI-writing "tics" in a markdown draft.
 
Categories, drawn from this project's own revision logs (Essay 3/4 dash
and phrase passes) plus the six-category framework from Roadmap #17
(Simplified Technical English / "AI slop" research):
 
  1. Em-dash density        — overuse flagged as an "AI slop" tell, broken
                               down further into weak "— and"/"— but"
                               clause-joins and a per-sentence pair/single/
                               irregular structure classification
  2. Inflated vocabulary    — delve, tapestry, robust, landscape, etc.
  3. Hedging / meta-commentary — phrases that gesture at significance
                                 instead of asserting it
  4. "Not just X, it's Y"   — the single most recognizable LLM formula
  5. Frozen verbs           — nominalizations ("make a decision" vs "decide")
  6. Run-on sentences       — length as a rough proxy, not a hard rule
 
Usage:
    python3 tic_scanner.py path/to/essay.md
    python3 tic_scanner.py path/to/essay.md --threshold-words 35
 
Deliberately excludes footnote/citation blocks (lines starting with "- ¹"
etc.) from em-dash counting, since citation-style dashes are a separate
structural convention, not prose rhetoric — this project's own revision
logs make that same distinction by hand.
 
This is a heuristic flagging tool, not a judge. Every flag needs a human
to decide whether it's doing real work (keep) or padding (cut) — same
discipline this project has applied by hand all along. False positives
are expected and fine; silently missing something is the worse failure.
"""
 
import argparse
import re
import sys
from pathlib import Path
 
INFLATED_VOCAB = [
    "delve", "tapestry", "robust", "landscape", "realm", "testament",
    "underscore", "boast", "seamless", "cutting-edge", "cutting edge",
    "transformative", "revolutionary", "groundbreaking", "unparalleled",
    "state-of-the-art", "world-class", "game-changing", "leverage",
    "synergy", "paradigm", "holistic", "unlock", "unleash", "elevate",
    "navigate", "foster", "harness", "pivotal", "myriad", "plethora",
    # merged from FareedKhan-dev/Detect-AI-text-Easily's ai_words.txt,
    # trimmed of entries too common in ordinary prose to be real signal
    # (core, facet, nuance, dynamics, implications, blend, unity, harmony)
    # and two that read as noise/dataset artifacts in the source list
    # ("Digital Bazaar", "Catering")
    "intrinsic", "integral", "facilitate", "culmination", "manifestation",
    "inherent", "confluence", "underlying", "intricate", "epitomize",
    "embodiment", "iteration", "synthesize", "amplify", "impetus",
    "catalyst", "cohesive", "prerequisite", "fusion", "quintessential",
    "symbiosis", "encompass", "unveil", "unravel", "emanate", "illuminate",
    "reverberate", "augment", "infuse", "extrapolate", "embody", "unify",
    "inflection", "instigate", "embark", "envisage", "elucidate",
    "substantiate", "resonate", "catalyze", "resilience", "evoke",
    "pinnacle", "evolve", "centerpiece", "subtlety", "immanent",
    "exemplify", "archetypal", "conceptualize", "reinforce", "mosaic",
    "comprehensive",
]
 
HEDGING_PHRASES = [
    "it's worth noting", "it is worth noting", "worth sitting with",
    "sit with", "worth being",
    "it's important to note", "it is important to note",
    "in many ways", "to some extent", "it's fair to say",
    "one could argue", "it's worth considering", "worth exploring",
    "this raises the question", "arguably", "in a sense",
    "it's worth remembering", "needless to say", "at the end of the day",
    "at the heart of", "in essence",
]
 
FROZEN_VERBS = {
    "make a decision": "decide",
    "conduct an analysis": "analyze",
    "provide assistance": "help",
    "make an assessment": "assess",
    "reach a conclusion": "conclude",
    "give consideration to": "consider",
    "carry out an investigation": "investigate",
    "make a determination": "determine",
    "provide clarification": "clarify",
    "engage in discussion": "discuss",
}
 
NOT_JUST_PATTERN = re.compile(
    r"\bnot (?:just|only)\b[^.!?]{0,40}\b(?:it'?s|it is|but)\b",
    re.IGNORECASE,
)
 
CITATION_LINE = re.compile(r"^\s*-\s*[¹²³⁴⁵⁶⁷⁸⁹⁰]")
REVISION_LOG_HEADING = re.compile(r"^\s*#+\s*Revision log\b", re.IGNORECASE)


def strip_revision_log(lines):
    """Drop everything from the '## Revision log' heading onward — it's
    development metadata that talks *about* these tics, not the published
    essay, and would otherwise get scanned as if it were prose."""
    for i, line in enumerate(lines):
        if REVISION_LOG_HEADING.match(line):
            return lines[:i]
    return lines


def strip_citation_lines(lines):
    """Return (prose_lines, citation_line_count) — matches this project's
    own hand-applied convention of excluding footnote dashes from prose counts."""
    prose = []
    citation_count = 0
    for line in lines:
        if CITATION_LINE.match(line):
            citation_count += 1
        else:
            prose.append(line)
    return prose, citation_count
 
 
def find_em_dashes(prose_text):
    return [m.start() for m in re.finditer("—", prose_text)]


WEAK_DASH_PATTERN = re.compile(r"—\s*(?:and|but)\b", re.IGNORECASE)


def find_weak_and_but_dashes(prose_text):
    """The clearest formulaic em-dash tell found by hand across every essay
    scanned so far: 'X — and Y' / 'X — but Y' joining two independent clauses
    where a period or comma does the same job more cleanly."""
    return [m.start() for m in WEAK_DASH_PATTERN.finditer(prose_text)]


def classify_dash_structure(prose_text):
    """Split into sentences and classify each one's dash count, mirroring the
    by-hand review method used on Essay 3/4: two dashes in one sentence are
    usually a genuine bracketing pair (a mid-sentence parenthetical, worth
    keeping); one dash is usually a single-sided appositive or clause-join
    that a colon or period could replace just as well; three or more is
    irregular and needs a manual read rather than a guess."""
    sentences = re.split(r"(?<=[.!?])\s+", prose_text)
    pairs, singles, irregular = [], [], []
    for s in sentences:
        count = s.count("—")
        if count == 2:
            pairs.append(s)
        elif count == 1:
            singles.append(s)
        elif count >= 3:
            irregular.append((count, s))
    return pairs, singles, irregular
 
 
def find_inflated_vocab(prose_text):
    hits = []
    for word in INFLATED_VOCAB:
        for m in re.finditer(r"\b" + re.escape(word) + r"\b", prose_text, re.IGNORECASE):
            hits.append((word, m.start()))
    return hits
 
 
def find_hedging(prose_text):
    hits = []
    for phrase in HEDGING_PHRASES:
        for m in re.finditer(re.escape(phrase), prose_text, re.IGNORECASE):
            hits.append((phrase, m.start()))
    return hits
 
 
def find_frozen_verbs(prose_text):
    hits = []
    for phrase, replacement in FROZEN_VERBS.items():
        for m in re.finditer(re.escape(phrase), prose_text, re.IGNORECASE):
            hits.append((phrase, replacement, m.start()))
    return hits
 
 
def find_not_just_pattern(prose_text):
    return [m.group(0) for m in NOT_JUST_PATTERN.finditer(prose_text)]
 
 
def find_long_sentences(prose_text, threshold_words):
    # crude sentence split — good enough for flagging, not for parsing
    sentences = re.split(r"(?<=[.!?])\s+", prose_text)
    long_ones = []
    for s in sentences:
        wc = len(s.split())
        if wc >= threshold_words:
            long_ones.append((wc, s.strip()[:100] + ("..." if len(s) > 100 else "")))
    return long_ones
 
 
def context_around(text, pos, width=60):
    start = max(0, pos - width)
    end = min(len(text), pos + width)
    snippet = text[start:end].replace("\n", " ")
    return f"...{snippet}..."
 
 
def main():
    # Windows terminals default to a non-UTF-8 codepage; without this, em-dashes
    # and superscript footnote markers print as mojibake instead of the real glyph.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Scan a markdown draft for AI writing tics.")
    parser.add_argument("file", type=str, help="Path to the markdown file")
    parser.add_argument("--threshold-words", type=int, default=35,
                         help="Sentence length (words) to flag as a run-on (default: 35)")
    parser.add_argument("--context-chars", type=int, default=50,
                         help="Characters of context to show around each hit (default: 50)")
    args = parser.parse_args()
 
    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
 
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    raw_lines = strip_revision_log(raw_lines)
    prose_lines, citation_dash_lines = strip_citation_lines(raw_lines)
    prose_text = "\n".join(prose_lines)
    word_count = len(prose_text.split())
 
    print(f"=== Scanning: {path.name} ===")
    print(f"Prose word count (citation lines excluded): {word_count}\n")
 
    # 1. Em-dashes
    dashes = find_em_dashes(prose_text)
    print(f"1. EM-DASHES: {len(dashes)} in prose "
          f"({citation_dash_lines} citation lines were excluded from this count, "
          f"regardless of how many dashes each contains)")
    if dashes:
        density = len(dashes) / max(word_count, 1) * 1000
        print(f"   Density: {density:.1f} per 1,000 words")
        flag = " ← worth a closer look" if density > 8 else ""
        if flag:
            print(f"  {flag}")

        weak_hits = find_weak_and_but_dashes(prose_text)
        print(f"   Weak \"— and\" / \"— but\" clause-joins: {len(weak_hits)} "
              f"(the clearest candidates for a period or comma)")
        for pos in weak_hits:
            print(f"     {context_around(prose_text, pos, args.context_chars)}")

        pairs, singles, irregular = classify_dash_structure(prose_text)
        print(f"   Dash structure by sentence: {len(pairs)} likely bracketing pair(s) "
              f"(2 dashes — probably functional), {len(singles)} single-sided "
              f"(candidate(s) for a colon or period), {len(irregular)} irregular "
              f"(3+ dashes — needs a manual read)")
        if singles:
            print("   Single-sided instances:")
            for s in singles:
                snippet = s.strip()[:100] + ("..." if len(s) > 100 else "")
                print(f"     {snippet}")
        if irregular:
            print("   Irregular instances:")
            for count, s in irregular:
                snippet = s.strip()[:100] + ("..." if len(s) > 100 else "")
                print(f"     [{count} dashes] {snippet}")
    print()
 
    # 2. Inflated vocabulary
    vocab_hits = find_inflated_vocab(prose_text)
    print(f"2. INFLATED VOCABULARY: {len(vocab_hits)} hits")
    for word, pos in vocab_hits:
        print(f"   '{word}' — {context_around(prose_text, pos, args.context_chars)}")
    print()
 
    # 3. Hedging phrases
    hedge_hits = find_hedging(prose_text)
    print(f"3. HEDGING / META-COMMENTARY: {len(hedge_hits)} hits")
    for phrase, pos in hedge_hits:
        print(f"   '{phrase}' — {context_around(prose_text, pos, args.context_chars)}")
    print()
 
    # 4. Not just X, it's Y
    formula_hits = find_not_just_pattern(prose_text)
    print(f"4. \"NOT JUST X, IT'S Y\" FORMULA: {len(formula_hits)} hits")
    for hit in formula_hits:
        print(f"   {hit}")
    print()
 
    # 5. Frozen verbs
    frozen_hits = find_frozen_verbs(prose_text)
    print(f"5. FROZEN VERBS (nominalizations): {len(frozen_hits)} hits")
    for phrase, replacement, pos in frozen_hits:
        print(f"   '{phrase}' → consider '{replacement}' — {context_around(prose_text, pos, args.context_chars)}")
    print()
 
    # 6. Long sentences
    long_sentences = find_long_sentences(prose_text, args.threshold_words)
    print(f"6. LONG SENTENCES (>{args.threshold_words} words): {len(long_sentences)} hits")
    for wc, snippet in long_sentences:
        print(f"   [{wc} words] {snippet}")
    print()
 
    total_flags = (len(dashes) + len(vocab_hits) + len(hedge_hits)
                   + len(formula_hits) + len(frozen_hits) + len(long_sentences))
    print(f"=== Total flags: {total_flags} ===")
    print("Reminder: every flag needs a human judgment call. This tool finds")
    print("candidates, not verdicts — same as every pass done by hand tonight.")
 
 
if __name__ == "__main__":
    main()