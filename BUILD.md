# Build and reproduction record

Version 1.0.0, 21 November 2026. This record covers the released bytes of this repository: the
manuscript `paper/main.pdf`, its sources and the replay program. Every digest below was computed
on the released files themselves, and `MANIFEST.sha256` plus `replay/SHA256SUMS` pin the same
bytes.

## Released bytes

| File | Size (bytes) | SHA-256 |
| --- | --- | --- |
| `paper/main.tex` | 44759 | `66e07649fb010c1dd5115a70447010b09f5602d3803279ce8016f50abd1ca1ab` |
| `paper/refs.bib` | 2362 | `dcf25882cc003db239fd14a17778e0b754787445d2c2461e5fe34392f3bb1555` |
| `paper/main.pdf` | 160763 | `3dfdcf009cd20cf115b32570c195ef86dc07b74a3994e01eebad204d35f6108c` |
| `replay/replay.py` | 22466 | `9f447e681545357281b316b43fa483e9d41631990c4f9644ce25375c1fa4a84b` |
| `replay/README.md` | 4694 | `95580bf4df44c3671c5eeeb80ad5d4896d7a6c33f1a928450b61fecb2042f78b` |
| `replay/SHA256SUMS` | 152 | `3fe3d409a01a297120e27d45a24be7d333c93771c158bd94d8c82a0b7a143bb2` |

The PDF has 15 pages. All files are UTF-8 or binary as appropriate and use LF line endings.

## Manuscript toolchain

- Compiler: Tectonic 0.17.0, the bundled TeX distribution it ships, driving `pdftex`-compatible
  XeTeX output; no local TeX installation is used.
- Document class `article`, 11 pt, with `amsmath`, `amssymb`, `amsthm`, `mathrsfs`, `microtype`,
  `hyperref`, `geometry` and `xcolor`, all from the bundled distribution.
- Bibliography: `plain` style, `refs.bib`, run by Tectonic's own BibTeX pass.
- Fixed build epoch: `SOURCE_DATE_EPOCH=1795132800` (2026-11-20T00:00:00Z), so that the PDF
  carries no build time.

Recipe, from the `paper/` directory:

```sh
SOURCE_DATE_EPOCH=1795132800 tectonic -X compile --keep-logs main.tex
```

Observed result: exit code 0; the log holds 0 `Overfull` lines, 0 `Underfull` lines, 0
`undefined` references or citations and no package warning; a second run from the same inputs
reproduces the PDF byte for byte, digest
`3dfdcf009cd20cf115b32570c195ef86dc07b74a3994e01eebad204d35f6108c`.

The released PDF is the post-review build. The review's prose findings were applied to
`paper/main.tex` before this build, and no theorem, constant, claim or conclusion changed.

## Replay

`replay/replay.py` needs Python 3.12 or later and nothing else: no third-party package, no data
file, no network and no random seed. From the repository root:

```sh
python -B replay/replay.py            # exit 0, 7 lines, empty standard error
python -B replay/replay.py --verify   # exit 0, 16 lines, empty standard error
python -B replay/replay.py --mutants  # exit 0, 20 lines, empty standard error
```

Observed on the released bytes: the default mode prints the two cubic witnesses with their bond
pins, the dimension-free general-`d` bound, the two dimension-one rows and the exact margins;
`--verify` adds the two complete cubic enumerators at `N = 4,5,6,7`, the `N = 7` against `N = 8`
comparison, the two-dimensional guards, the independent colourings, the independent Raney
coefficients and the second interval certification of every bond pin; `--mutants` refuses all
nineteen corrupted certificates with child exit one and closes with
`CERTIFIED: 19 mutants refused with child exit 1`.

A single named corruption can be exercised directly, for example
`python -B replay/replay.py --mutant general-one-scale-below-one`, which exits one with
`REJECTED general-one-scale-admissible`.

## Continuous integration

`.github/workflows/ci.yml` installs the pinned Tectonic 0.17.0 release after checking its
archive digest, rebuilds the manuscript with the epoch above, checks the build log, compares the
rebuilt text with the released PDF, and then verifies both pin files, builds the release archive
from the commit, unpacks it and runs the replay's three modes on the unpacked copy.

## Byte custody

```sh
sha256sum -c MANIFEST.sha256
(cd replay && sha256sum -c SHA256SUMS)
```

`MANIFEST.sha256` lists every tracked file except itself; `replay/SHA256SUMS` lists the two files
of the replay directory. Both lists were compared byte for byte against the released tree with
Python's `hashlib` and report zero mismatches, and the continuous-integration job reruns
`sha256sum -c` on both. The deposited supplement archive is `git archive` of the release tag, so
its members are these bytes.
