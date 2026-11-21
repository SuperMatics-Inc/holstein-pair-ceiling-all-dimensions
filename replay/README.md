# Cubic and general-dimensional Holstein pair-ceiling certificate

This supplement accompanies Davis Rens, *Certified cubic and general-dimensional strong-coupling ceilings for electronic pair correlations in the Holstein model*.

## Claims and scope

For the spinful nearest-neighbour Holstein model, with U=F^2/K>0, hopping t>=0, every phonon frequency Omega>0 and every real common chemical potential:

- On (Z/NZ)^3, all N>=4: k_B T_pair <= 27900 t^2/U.
- On (Z/NZ)^3, even N>=4: k_B T_pair <= 22800 t^2/U.
- For every integer d>=1, all N>=4: k_B T_pair <= 5750 d^3 t^2/U.
- For every integer d>=1, even N>=4: k_B T_pair <= 4600 d^3 t^2/U.

The cubic distinct-site pair prefactor is 11/100; the general-dimensional prefactor is 9/40. Both have exponential decay ratio 99/100. The analytical theorem also transfers to translation-invariant thermodynamic canonical limits at interior density, including balanced separately fixed spin sectors. It does not assert a uniform finite-volume canonical bound or a result for imbalanced spin sectors.

These are pairing-correlation ceilings, not measured or fitted T_c values, not predictions that ordering occurs below the ceiling, and not globally optimal constants. The finite arithmetic witnesses are checked in exact rational and outward-interval arithmetic. The analytical extension rests on an independent scientific review of its local inputs and dimensional extension. This independent review is not journal peer review; the manuscript has not been peer reviewed.

## Files

- `replay.py`: standalone Python standard-library certificate and independent checks. It requires no data files, network, random seeds or external packages.
- `README.md`: these instructions.
- `SHA256SUMS`: SHA-256 digests of the preceding two files, excluding the checksum file itself.

The replay is byte-identical to the reviewed-and-corrected proof-package replay: 22466 bytes, SHA-256 `9f447e681545357281b316b43fa483e9d41631990c4f9644ce25375c1fa4a84b`. Copy it as bytes, not through a newline-normalizing text tool. No logs, backups or mutable result files are required in this supplement.

## Run

Use Python 3.12 or later. From this directory:

```sh
python -B replay.py
python -B replay.py --verify
python -B replay.py --mutants
```

The certificate imports no third-party package. `-B` prevents generated `__pycache__` files. Run at most one full enumeration at a time.

Default mode certifies the two cubic witnesses and the general-dimensional bound. `--verify` additionally compares two complete small-support enumerators at N=4,5,6,7, checks N=7 against N=8, reproduces the two-dimensional class guards, constructs independent proper colourings, independently re-derives Raney coefficients, and independently certifies every bond interval.

`--mutants` launches 19 fresh child processes. Each corrupted certificate must return exit 1 and end with a meaningful `REJECTED` guard. The harness returns exit 0 only if every corrupted child is refused. A named mutation can also be exercised directly:

```sh
python -B replay.py --mutant general-one-scale-below-one
```

That example must return exit 1 with `REJECTED general-one-scale-admissible`. Successful certificate and verification invocations return exit 0; a failed inequality returns exit 1. Numerical display output is calculated from already certified rational bounds, never used as an acceptance input.

## Certification evidence

The post-correction `--verify` and `--mutants` invocations each returned exit 0. All 19 corrupted children returned exit 1. The executed source and this supplementary replay have the identical digest above; the exact command outputs and scientific-review provenance are recorded in the accompanying build and claims records.

The two cubic KP margins exceed 0.000085641 (even) and 0.000137168 (all sizes); the dimension-free d>=2 margin exceeds 0.004263714. All 14 bond pins are checked with both outward dyadic Taylor/Newton intervals and independent unrounded rational Taylor/integer-square-root intervals. The k<=6 rooted count maxima have 21/23 classes and exact sums 337498/337573.

No floating-point proof decisions, finite-frequency approximation, unproved lower colour count, omitted vertex factor, or relaxed multiplicity is used. The source budget retains the full implicit Jacobian, and explicit Cy>=1 scale guards are exercised by two rejecting mutants.

## Byte custody

To validate the manifest from this directory on a system with `sha256sum`:

```sh
sha256sum -c SHA256SUMS
```

A successful checksum comparison is byte custody only, not a proof of the analytical lemmas. The certificate and the manuscript supply those distinct forms of evidence.
