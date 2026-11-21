"""Check that a released PDF carries the manuscript's title, identifiers and constants.

Usage: python3 ci/verify_text.py <extracted-text-file>

The text file is the output of `pdftotext -raw` on `paper/main.pdf`. Every marker is
compared after folding case and dropping everything except letters and digits, so line
breaks, hyphenation and inter-word spacing in the extraction cannot hide a marker.
"""

import re
import sys

TITLE = "Certified cubic and general-dimensional strong-coupling ceilings for electronic pair"
SUBTITLE = "correlations in the Holstein model"

MARKERS = [
    TITLE,
    SUBTITLE,
    "Davis Rens",
    "SuperMatics Inc.",
    "0000-0001-5839-5197",
    "This preprint has not been peer reviewed.",

    "Koteck",  # a cited work appears in the bibliography
    # the two ceilings in three dimensions
    "22800",
    "27900",
    # the general-dimension constants
    "5750",
    "4600",
    # the exact margins quoted in the abstract and the results

    "11/100",
    "9/40",
    "99/100",
    # the integer citation count and its two fractional forms
    "63700992",
    "1769472/775",
    "1327104/475",
    # the two earlier records
    "10.5281/zenodo.24412193",
    "10.5281/zenodo.24414616",
]


def norm(text: str) -> str:
    return re.sub(r"[^0-9a-z]", "", text.lower())


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_text.py <extracted-text-file>", file=sys.stderr)
        return 2
    with open(sys.argv[1], encoding="utf-8", errors="replace") as handle:
        text = norm(handle.read())
    missing = [marker for marker in MARKERS if norm(marker) not in text]
    for marker in MARKERS:
        print(f"{'ok  ' if norm(marker) in text else 'MISS'} {marker}")
    phrase = norm("This preprint has not been peer reviewed.")
    count = text.count(phrase)
    print(f"disclosure phrase occurrences: {count}")
    if count != 1:
        print("the disclosure phrase must appear exactly once", file=sys.stderr)
        return 1
    if missing:
        print(f"missing markers: {missing}", file=sys.stderr)
        return 1
    print(f"all {len(MARKERS)} markers present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
