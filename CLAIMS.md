# Claims and evidence map

Manuscript: Davis Rens, *Certified cubic and general-dimensional strong-coupling ceilings for
electronic pair correlations in the Holstein model*, preprint
[10.5281/zenodo.24417313](https://doi.org/10.5281/zenodo.24417313), with the replay supplement
[10.5281/zenodo.24417315](https://doi.org/10.5281/zenodo.24417315). Version 1.0.0, released
21 November 2026.

## Status and boundaries

Every analytical statement below is proved in the manuscript, and the whole argument was read
in an independent scientific review of the proof package, whose findings were corrected in the
released text. The finite arithmetic witnesses are verified by `replay/replay.py` in exact
rational or outward-interval arithmetic, with two independently implemented arithmetic methods
for the bond pins and two complete enumerators for the support counts. That review is not
journal peer review, and the replay does not formalize the analysis. The manuscript states once,
verbatim: "This preprint has not been peer reviewed."

The numerical exploration that chose the scales is not a global optimality proof. No measured,
fitted or generated material transition temperature is claimed, and no phase transition is
proved or excluded.

## Model and units

The spinful nearest-neighbour Holstein model on `(Z/NZ)^d`, `N >= 4`, with centred coupling
`-F Q_x (n_x - 1)`, `U = F^2/K > 0`, `Omega = sqrt(K/M) > 0`, no direct electron-electron
interaction, hopping `t >= 0` and an arbitrary real common chemical potential. Completing the
oscillator square gives the electronic atomic term `(U/2) N_odd - mu_c N_e`, up to the stated
constant and chemical-potential convention.

Every ceiling has the form `k_B T_pair <= C t^2/U`. The constant `C` is dimensionless and
`t^2/U` is an energy; `beta U` and `beta t` are dimensionless. No unaccounted factor of `hbar`,
`2 pi`, `k_B` or two enters the conversion. `T_pair` denotes an exponential pair-correlation
decay ceiling of one two-point function, not a finite-volume singularity and not a determined
superconducting transition temperature.

## Claim-by-claim map

| Claim | Where in the manuscript | Evidence in this repository | Classification |
| --- | --- | --- | --- |
| All-size cubic ceiling `C = 27900`, `N >= 4` | Abstract; Theorem 1; the cubic budget section | Exact classwise and source budgets in the manuscript; `replay.py` bond pins and the cubic witness | Proved analytically; finite witness replayed |
| Even-size cubic ceiling `C = 22800`, `N >= 4` | Abstract; Theorem 1; the parameter table | The same budgets with the even classwise table and the six-colour tail; `replay.py` even witness | Proved analytically; finite witness replayed |
| Cubic pair prefactor `11/100` and decay ratio `99/100` | Abstract; Theorem 1; the Kotecký-Preiss lemma | Vertex deletion and `2 ln B <= 11/50`; the prefactor and strict-decay guards of `replay.py` | Proved; arms replayed |
| `C_all(d) = 5750 d^3` and `C_even(d) = 4600 d^3` for every integer `d >= 1` | Theorem 2; the general-dimensional section | The dimension-free `d >= 2` majorant and the separate `d = 1` argument; the general witness of `replay.py` | Proved analytically; finite witness replayed; not extrapolated from sampled dimensions |
| General-dimensional prefactor `9/40`, same decay ratio | Theorem 2; the general-dimensional section | `2 ln(5/4) <= 9/20`; the log-series and strict-decay guards | Proved; arms replayed |
| Uniformity in `Omega > 0` and in a real common chemical potential | Abstract; the model, contour and support sections; Appendix A | Chronological oscillator contraction re-displayed in Appendix A; exact fugacity supremum at `z = 1` | Proved shared inputs and dimensional extension; not a finite-frequency numerical scan |
| The exact two-site spectrum carries `3 q_b^2`, not `4 q_b^2` | The two-site spectrum lemma | Five particle-number sectors of the sixteen-state bond Hamiltonian; the bond pins | Proved algebraically; replayed |
| Physical bridges have at least two hops, and `m >= k + number_of_bridges` | The multiplicity lemma | Bridge parity; the `bridge-m-equals-k` mutant is refused | Proved structural bound |
| Degree `p = 2d` governs support growth, `c = 2d` even or `2d + 1` odd governs Hölder | The colour lemma; the Raney lemma | Recursive colour construction and independent Raney derivation in `--verify` | Proved dimension dependence; sampled colourings supplementary |
| One scale per valid support class with `ell = sqrt(Cy) >= 1` | The weight section; the scale paragraphs of the general section | `general-one-scale-below-one` and `general-d1-scale-below-one` mutants refused | Proved parametrisation; guards replayed |
| Exact `k <= 6` classwise counts, 21 even and 23 all classes, sums 337498 and 337573 | The counting section | Independent connected-edge enumerators at `N = 4,5,6,7`, the `N = 7` against `N = 8` comparison and the two-dimensional guards in `--verify` | Verified finite integers plus a proved lift argument |
| Fourteen bond pins over 101 accepted cells under each arithmetic method | The cubic budget section; the certificate section | `certify_bond`: outward dyadic Taylor and Newton intervals, and independent unrounded rational Taylor with integer square roots | Verified outward bounds, not floating-point sampling |
| Cubic Kotecký-Preiss margins above `0.000085641` (even) and `0.000137168` (all sizes) | The budget table | Printed by every mode of `replay.py` as a display of rational margins | Verified rational arithmetic |
| The source count obeys `P = 1 + w_p P^(p-1) S^2`, `S = (1 - w_s P^p)^(-1)`, `G = P^p S^2` | The source section | Full source Jacobian with independently re-derived derivatives; `source-scale-ten`, `source-den-sign` and `independent-source-jacobian` mutants refused | Proved combinatorial majorant; parameter inequalities replayed |
| General `d >= 2` margin above `0.004263714` | The general-dimensional section | Exact dimension-free polynomial, Taylor and logarithm reduction; source derivatives cross-checked at `d = 2, 3, 4, 7, 100` | Verified arithmetic on a proved all-`d` inequality |
| Thermodynamic canonical transfer at interior density, including balanced fixed spin sectors | The canonical-transfer section | The fixed-`d` block-subdivision equivalence of ensembles | Proved under the stated translation-invariance and ensemble conditions; not a uniform finite-volume sector bound |
| The Cauchy source disk is `|xi| <= tau/400000` | The canonical-transfer section | `xi_0 = tau/200000` and Cauchy radius `xi_0/2` | Proved corrected source estimate |
| All nineteen corrupted certificates are refused with child exit one, and the harness exits zero | The certificate section; `replay/README.md` | `replay.py --mutants` runs each corruption in a fresh child process with a named `REJECTED` guard | Exercised arithmetic robustness check; not scientific peer review |
| The earlier all-size cubic constant is 63700992, reduced by the exact factor `1769472/775` | The comparison paragraphs | Released preprint [10.5281/zenodo.24412193](https://doi.org/10.5281/zenodo.24412193); exact arithmetic | Source constant plus a calculated ratio, not a measured improvement |

## Shared inputs and their citations

The dimension-independent inputs come from the released two-dimensional chain, preprint
[10.5281/zenodo.24414616](https://doi.org/10.5281/zenodo.24414616): the chronological Lang-Firsov
representation and the normalized oscillator contraction; bridge parity and the colour-class
Hölder decoupling with the pair-source norm bound; the exact bond spectrum, its fugacity
supremum and the uniform `beta U` bound; the labelled depth-first exploration and the
physical and source multigraphs; and the Kotecký-Preiss deletion, the source disk and the
canonical-transfer argument.

The present manuscript displays the dimension-dependent construction and the corrected source
budget instead of importing two-dimensional constants. Its bibliography carries primary
references for the Holstein model, Lang-Firsov context, abstract polymer expansions, ensemble
equivalence and the edge-colouring theorem. No new quantitative result from another paper is
introduced.

## Obstruction that was resolved, and leads that are not used

An earlier scratch computation claimed an obstruction for every `C`. It is not real: at fixed
`y > 0` the weight `B M(c,y)^(1/c) / (q sqrt(Cy))` tends to zero as `C` grows, and the condition
`ell = sqrt(Cy) >= 1` is a lower scale constraint whose reversal cannot give a no-go. That work
also minimized over colour counts in an inadmissible way and omitted the vertex factor `B` from
the tail weight.

The retained proof uses a valid colour upper bound, including `c = 7` for the all-size cubic
tails. It does not promote earlier floating-point `d^3` constants, low-colour minima or a fixed-`q`
expression without the `b` variable into evidence.

## What is not claimed

Global parameter optimality; a lower bound on ordering; material qualification; a uniform
finite-volume fixed-sector canonical bound; transfer for imbalanced spin sectors; formal
verification of the analysis; journal peer review; publication in a journal.

## Custody

`replay/SHA256SUMS` binds `replay.py` and its instructions, and `MANIFEST.sha256` binds every
other file of this repository. Checksum custody does not by itself prove the theorem.
