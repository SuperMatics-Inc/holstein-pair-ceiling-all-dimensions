# Certified cubic and general-dimensional strong-coupling ceilings for electronic pair correlations in the Holstein model

Davis Rens, SuperMatics Inc., [ORCID 0000-0001-5839-5197](https://orcid.org/0000-0001-5839-5197)

| | |
| --- | --- |
| Preprint | [10.5281/zenodo.24417313](https://doi.org/10.5281/zenodo.24417313) |
| Replay supplement | [10.5281/zenodo.24417315](https://doi.org/10.5281/zenodo.24417315) |
| Version | 1.0.0, 21 November 2026 |
| Manuscript | [`paper/main.pdf`](paper/main.pdf), 15 pages |

This repository is the tagged release tree of that preprint. It holds the reviewed
manuscript source, the released PDF and the complete replay supplement, pinned byte for
byte through [`MANIFEST.sha256`](MANIFEST.sha256) and [`replay/SHA256SUMS`](replay/SHA256SUMS).

## The result

For the spinful nearest-neighbour Holstein model on the cubic torus `(Z/NZ)^3`, with
`U = F^2/K > 0`, hopping `t >= 0`, every phonon frequency `Omega > 0`, every real common
chemical potential and every side `N >= 4`:

- if `beta t^2/U <= 1/27900`, then for every pair `x != y` the equal-time on-site pair
  correlations obey `|<Delta_x^dag Delta_y>| <= (11/100)(99/100)^dist(x,y)`, their rows
  are uniformly summable, and the clustering temperature of that correlator obeys
  `k_B T_pair <= 27900 t^2/U`;
- on even cubic tori the same decay holds under the weaker hypothesis
  `beta t^2/U <= 1/22800`, hence `k_B T_pair <= 22800 t^2/U`.

For every integer `d >= 1` and every `N >= 4` the same scheme gives the ceilings
`C_all(d) = 5750 d^3` and `C_even(d) = 4600 d^3`, with prefactor `9/40` and the same decay
ratio `99/100`. Every statement is uniform in `Omega > 0`, in the volume and in the real
common chemical potential, with no smallness condition on `t/U`, and transfers to
translation-invariant thermodynamic canonical limits at interior density, including
balanced separately fixed spin sectors.

The earlier released hypercubic constant is `C_old(d) = 442368 d^2 (d+1)^2`, with
`C_old(3) = 63700992`. The cubic constant here is smaller by the exact factor
`1769472/775 = 2283.19...` on all cubic tori and `1327104/475 = 2793.90...` on even cubic
tori, and the growth of the constant with the dimension falls from the fourth power to the
cube.

The proof combines an exact signless oscillator contraction in the Lang-Firsov form, a
connected-support expansion of the pair correlation with a signless trajectory majorant,
the exact sixteen-state two-site bond spectrum with its sector multiplicities and
half-filling fugacity supremum, a bridge parity, an explicit proper edge colouring and a
Schatten-Hölder decoupling, exact rooted-support enumerators at `k <= 6` with a degree-`2d`
Raney tree tail, and the Kotecký-Preiss vertex criterion for a source-augmented polymer
expansion.

## What the paper does not claim

The bounds are on `T_pair`, a clustering temperature of one two-point function, never on a
measured critical temperature. No material is claimed and no superconductivity is claimed;
no phase transition is proved or excluded. The constants are not globally optimal, and the
`O(d^3)` theorem is not an optimal asymptotic-dimensionality assertion. The analytical
arguments are supplemented by the finite arithmetic checks below; neither those checks nor
the independent reviews amount to journal peer review or formal proof-assistant
verification.

The finite arithmetic witnesses are checked by a certificate program in exact rational and
outward-interval arithmetic. It verifies arithmetic, not analysis.

## Contents

| Path | What it is |
| --- | --- |
| `paper/main.pdf` | The released manuscript, 15 pages. |
| `paper/main.tex` | The LaTeX source that produces that PDF. |
| `paper/refs.bib` | The bibliography. |
| `replay/replay.py` | The certificate program: standard library only, no data file, no network. |
| `replay/README.md` | What the replay certifies, how to run it and its byte custody. |
| `replay/SHA256SUMS` | Pins for the two files of the replay directory. |
| `MANIFEST.sha256` | Pins for every other tracked file of this repository. |
| `CLAIMS.md` | The claim list, with each statement labelled and its evidence named. |
| `BUILD.md` | How the PDF is built, with the compiler version and the pinned build inputs. |
| `CITATION.cff` | Citation metadata for the preprint and the supplement. |
| `LICENSE` | Apache-2.0 for the code, CC-BY-4.0 for the manuscript, as stated in its first lines. |

## Reproduce

### The replay

Python 3.12 or later; nothing else. From the root of an unpacked release:

```sh
python -B replay/replay.py
python -B replay/replay.py --verify
python -B replay/replay.py --mutants
```

The default mode prints seven lines: six verified results, namely the two cubic witnesses with their bond pins,
the dimension-free general-`d` bound, the two dimension-one rows and the exact rational
margins, followed by a one-line summary of the certificate. `--verify` additionally runs two
complete cubic enumerators at `N = 4,5,6,7`, an
`N = 7` against `N = 8` comparison, the two-dimensional count guards, independent
recursive edge colourings, an independent Raney-coefficient derivation and a second,
independently implemented interval certification of every bond pin. `--mutants` corrupts
nineteen guarded claims one at a time in fresh child processes and requires each to exit
one with a named rejection; the harness itself returns zero only when all nineteen are
rejected. Successful runs exit 0 and print nothing on standard error.

### The paper

```sh
cd paper
SOURCE_DATE_EPOCH=1795132800 tectonic -X compile --keep-logs main.tex
```

`Tectonic 0.17.0` with that fixed epoch reproduces the released PDF; the log has no
overfull box, no underfull box and no undefined reference. [`BUILD.md`](BUILD.md) records
the compiler, the driver, the pinned epoch and the digest of every build input.

### Continuous integration

[`.github/workflows/ci.yml`](.github/workflows/ci.yml) pins the Tectonic release it
installs, rebuilds the manuscript, checks the rebuilt text against the released PDF,
verifies both manifests, builds the release archive from the commit, unpacks it and runs
the replay's default, `--verify` and `--mutants` modes on the unpacked copy.

## Byte custody

Every released file is a copy of reviewed bytes, and `MANIFEST.sha256` plus
`replay/SHA256SUMS` pin all of them except the two manifests themselves:

```sh
sha256sum -c MANIFEST.sha256
(cd replay && sha256sum -c SHA256SUMS)
```

The deposited supplement archive is `git archive` of the `v1.0.0` tag, so its members are
the files listed by `git ls-files` at that commit, unchanged.

## Licences

The manuscript (`paper/main.tex`, `paper/refs.bib`, `paper/main.pdf`) is licensed under
Creative Commons Attribution 4.0 International (CC-BY-4.0). The replay program and all
remaining files are licensed under the Apache License 2.0. The first lines of
[`LICENSE`](LICENSE) state that split; the full Apache-2.0 text follows.

## Review and AI assistance

AI research agents generated the proofs, the certificate program and the manuscript drafts
and edits under D. Rens' direction and review, and separate AI systems carried out the
independent reviews of the argument and of the certificate program, whose comments led to
several corrections. This preprint has not been peer reviewed.
