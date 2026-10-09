# Remainder-Growth Class (RGC) | 2026-10-09

**Discovery ID:** RGC-2026-10-09
**Session:** 2026-10-09T17:40:00Z-rgc
**Author:** Haley Ann Bird (Fishers, IN) · GitHub `sENZ5hFx` · autonomous Grok agent
**SHA-256 of `rgc_result.json`:** `862b915ba6e769b3cc06d633f9ee37fa7e0f7ba35498cac9a5c4a6286a47bf5f`
**Novelty (capped):** 0.29
**Coherence:** 0.80
**IP Readiness:** Logged
**Prior art verified:** yes (archive subtracted, including DPC-2026-10-07, which queued this class and did not mint it)

Research-stage classification. **Not a physical discovery, not peer review, not a patent.** Timestamp is not filing. Copyright may attach to original expression on fixation. This page is not a filing receipt, priority date, scientific validation, or exclusive right in a natural hypothesis.

Grok by xAI (non-ownership; structural synthesis aid only).

## Core insight

Added observational effort grows the unnamed remainder faster than the named set. Search effort is often granted the privilege of being a closer of the unknown. In an RGC instance the derivative has the other sign: marginal effort adds unnamed entities faster than named ones, so the gap between discovered and discoverable widens.

Kill rule: if the remainder channel is saturated — discovery coefficient α ≤ 0, or a nested rarefaction slope ≈ 0 — the instance leaves RGC. Further effort does not manufacture remainder.

Score: `40 × outruns × unsaturated × derivative_measured × evidence × (1 − spoken) × (1 − prior_overlap)`.

A single examined slice that is entirely new is not a measured derivative. `derivative_measured` keeps it from outranking an α gap.

## Why this session exists

The standing prompt asks for undiscovered things across every realm in a 10-plane, ~150-field taxonomy. Coverage Hole Lattice already owns the 150-mint generator. CLOSED-2026-09-30 and the later CLOSURES make another 150-mint protocol-invalid.

Skill `high-agency-partner` rule 7: if the leftover from the last session was never given a Discovery ID, that leftover is the session.

On 2026-10-07, Denominator-Privilege Class (`DPC-2026-10-07`) queued, and did not mint:

> Remainder-Growth Class: effort grows unnamed remainder faster than the named set. Different kill rule (saturation).

No GitHub repo and no Notion Discovery ID existed for RGC on 2026-10-09 (GitHub user search; Notion search of the IP log). This session writes that ID.

DPC owns a published quantity whose denominator is a construct treated as observed. Rewriting the denom rewrites the number with no object moving. RGC owns the derivative of the unnamed stock with respect to effort. FCC owns whether addressable frontiers coincide, not this derivative. Species-accumulation curves (Gotelli & Colwell; Chao) own the method. RGC is not that method. It is the class of censuses where the remainder channel is still climbing and outrunning the named channel.

## Live ranking

| Rank | ID | Score | Ruling | Role | Realm |
|---:|---|---:|---|---|---|
| 01 | unbinned_widening_gap | 9.6657 | keep | primary | land |
| 02 | mar_del_plata_copepods | 5.6886 | keep | runner | ocean |
| — | archaea_host_genome_saturated | 0.0196 | control | control | land |
| — | rarefaction_plateau_namesake | 0.0008 | control | control | humans |

`controls_ok = true` (both < 1.0). The copepod slice does not outrank the measured α floor. Asserted by `rgc_score.py` before exit.

## Primary — unbinned contigs outrun genomes, and the authors say the gap widens

Prasoodanan, Maistrenko, Fullam, Mende, Kartal, Coelho, Spang, Bork & Schmidt, *Nature Microbiology* **11**, 1437–1449 (2026). DOI [10.1038/s41564-026-02314-6](https://doi.org/10.1038/s41564-026-02314-6). Online early April 2026.

Retrieved figures, not recomputed here:

| Object | Retrieved value |
|---|---|
| Metagenomes | 92,187 |
| Marker-gene sequences clustered | 502 million, 130 marker genes |
| Predicted bacterial species-level clades | ~705,000 |
| Predicted archaeal species-level clades | ~27,000 |
| Cultivated representatives | ~20,000 bacterial; ~800 archaeal |
| Genome-based representation | 17.8% of bacterial species-level diversity; 24.6% of archaeal |
| Not captured by isolates or MAGs | up to ~75–80% of species-level clusters |
| Undescribed phyla discoverable in this dataset | 145 bacterial; 10 archaeal |
| Unbinned discovery coefficient | α ≥ 0.5 across most habitats |
| Hotspots (soil, wetland, rhizosphere, freshwater, non-mammalian guts) | α ≥ 0.8, "virtually no slowdown" |

The paper's own sentence (retrieved via the article page): the difference in discovery coefficients "suggests a widening gap between discovered (genomically represented) and discoverable (unbinned) diversity, as the latter will continue to outpace the former," and "the existing large discovery gap between binned and unbinned contigs will continue to widen."

`remainder_derivative` on the published floors (α ≥ 0.5; soil α ≥ 0.8), with **no invented point estimate** for the MAG coefficient: mode `remainder_floor_only`, `rgc_holds=True`.

**RGC remainder:** more public metagenomes are not closing the unnamed set. They feed the unbinned channel faster than the genome channel. DPC, on this same paper, owns only the privilege of treating today's discoverable set as "all microbes." That privilege was logged yesterday. It is not re-issued.

Not claimed: a new species count, that MAGs are useless, or that 705,000 is a headcount of living species rather than a clustering prediction.

Spoken inside this one paper, hence `spoken=0.50`. Overlap with DPC on the same source, hence `prior_overlap=0.36`. The score is 9.67 because those penalties are real. Inflating them away would fake novelty.

## Runner — one canyon slice, derivative not yet measured

Nippon Foundation–Nekton Ocean Census, press release 1 October 2026: [57 new marine species](https://oceancensus.org/press-release-57-new-marine-species-discovered-in-argentinas-submarine-canyons/). Workshop 13–24 July 2026, Universidad Maimónides, Buenos Aires. Samples from the Schmidt Ocean Institute *Falkor (too)* expedition, July–August 2025, Mar del Plata Canyon.

Retrieved sentence: taxonomists examined just 10% of the collected harpacticoid samples; every specimen examined was a species new to science; 20 new species and 1 new genus. Workshop total: 57 species and 5 genera (20 copepods, 22 echinoderms, 14 cnidarians, 1 scaphopod).

`single_bin_novelty(examined_fraction=0.10, novelty_rate=1.0)`: mode `single_bin_consistent`, `derivative_measured=False`.

**RGC remainder:** the first tenth did not spend the unnamed stock down. It returned a novelty rate of 1. That is consistent with remainder growth and is not a measurement of it. The next tenths have not been scored. Score 5.6886, role runner, status unsolved.

Not claimed: that the unexamined 90% will also be 100% new; that these are Code-published names (the release is a workshop identification); that copepods worldwide are undescribed at this rate.

## Controls that must score near zero

- **Host-habitat archaeal genomes, same paper.** Genome-based discovery of archaeal species fully saturated (α ≤ 0) or approaching saturation in most host-associated and anthropogenic habitats, including human infant gut, oral cavity, and skin. Adding samples is not expected to increase metagenomic representation of that reference-recoverable set. `remainder_derivative(..., 0.0, 0.0)`: mode `saturated_kill`, kill fired. Score **0.0196**.
- **Textbook rarefaction plateau.** Gotelli & Colwell accumulation / Chao asymptote. A terminal slope of ~0 is the kill definition, not an instance. Score **0.0008**. RGC is not the rediscovery of rarefaction. Species-accumulation curves, the taxonomic impediment, and Chao estimators are why novelty is capped at 0.29.

If a later re-analysis of the 92,187 metagenomes shows unbinned α ≤ 0 in the habitats now marked ≥ 0.5, the primary leaves RGC.

## Iteration

`remainder_derivative` refuses a fake MAG α. Where the source gives only a floor, the mode is `remainder_floor_only`.

Where a coarse channel is at α ≤ 0 and a finer channel is still at the unbinned floor, RGC still holds on the fine channel, and the function sets `queued_false_saturation=True`. That is a different kill rule: the finer channel was already inside the likelihood, and someone reported the coarse plateau as closure.

| ID | Mode | RGC holds | Kill fired | FSC queued |
|---|---|---|---|---|
| unbinned_vs_mag_floor | remainder_floor_only | yes | no | no |
| soil_hotspot_floor | remainder_floor_only | yes | no | no |
| archaea_host_genome_saturated | saturated_kill | no | yes | no |
| false_saturation_queue | remainder_outruns | yes | no | yes |
| mar_del_plata_copepods | single_bin_consistent | yes (prediction) | no | no |
| saturated_drawer_control | saturated_kill | no | yes | no |

**False-Saturation Class is queued, not minted.**

## Per-realm — instances, absences, and what is not RGC

These are not 150 discoveries. A realm with no retrieved derivative is an absence, not a mint.

### Land
- **Instance (primary):** unbinned prokaryotic diversity, especially soils, wetlands, rhizosphere, freshwater. α ≥ 0.8 in those hotspots, inside the same paper. Not a second independent replication.
- **Not re-issued:** ectomycorrhizal dark taxa at 83% (van Galen et al., *Current Biology*, 9 Jun 2025). That is a stock. DPC already ranked it. No new d(unnamed)/d(effort) was retrieved today.
- **Unproved:** that the 145 bacterial phyla survive cultured taxonomy; that eDNA or marker clusters equal species.

### Ocean
- **Instance (runner):** Mar del Plata harpacticoids, first 10%, novelty rate 1, derivative unmeasured.
- **Not re-issued:** CCZ vOTU unmatched fraction (PDC runner). Dark oxygen (not a finding; not an RGC derivative). Seafloor visual coverage (DPC runner: three denominators, one slogan).
- **Unproved:** that the unexamined 90% matches the first 10%.

### Animals
- The copepod runner is the animal instance. Sperm-whale coda counts grew because the named repertoire was enlarged. That is a numerator growing, not an unnamed remainder outrunning a named set. Not RGC. Not re-issued from DPC.

### Outer space
- **No RGC instance retrieved.** η⊕ rewritten by completeness is DPC. Hubble tension is PDC (two operators, one quantity). No 2026 survey was retrieved in which the unnamed astronomical remainder's discovery coefficient stays above the named channel's. Absence is the result. It is not a discovery about dark matter, Population III stars, or Little Red Dots.

### Humans
- **No RGC instance retrieved.** Inconsistent income denominators are DPC. Denominator neglect is a 1994 cognitive bias and was a DPC control. A saturated accumulation curve is this session's method control, score ~0.
- **Unproved, and not minted:** any claim that clinical rare-disease catalogs or psychiatric taxonomies are remainder-growing. Those series were not retrieved today.

### Earth interior, icy moons, consciousness
- No retrieved α. Not minted. ULVZ coverage and LLSVP origin stay with prior classes (PDC / RJC). Biosignature claims stay unproved. Consciousness and sleep stay unsolved and are not RGC objects.

## Not claimed

- Not 150 per-realm discoveries. The taxonomy in the prompt is a catalogue of fields, not a partition of existence. Treating it as exhaustive would be a mint the closures already forbid.
- Not a new count of microbial or canyon species.
- Not DPC, FCC, DCC, OAC, FPC, PDC, or ANC re-issued under a new name.
- Not that α = 0.25 or any other unpublished point estimate. Floors only, where floors were published.
- Not that workshop identifications are zoological acts under the Code.
- Not False-Saturation Class (queued).
- Not rarefaction, Chao estimators, or the taxonomic impediment as a finding.
- Not dark oxygen, plant sentience, xenocortical minds, or a unification of the word "dark."
- Not a patent. A hypothesis about how censuses behave is not a patentable invention. Timestamp ≠ filing.

## Archive subtracted

Dark Biosphere, TAC, Cadence Mismatch, NCR, FAC, CIC, JAC, IOA, DIC, PPC, UCC, DCC, FCC, OAC, UPRC, CIP, TPC, CMC, EFC, IPC, SBC, IRC, SEC, RJC, ANC, UEDP, FPC, PDC, DPC, RD Plane-Split, CHL, CLOSED-2026-09-30, CLOSED-2026-10-02, CLOSED-2026-10-04, CLOSED-2026-10-05, CLOSED-2026-10-07.

Novelty capped at 0.29 because accumulation curves, Chao estimation, the taxonomic impediment, and Schmidt et al. 2026 already state that unbinned discovery outpaces genomes. The class is the cross-census derivative plus the saturation kill, not those results.

## Testables

1. Recompute unbinned vs MAG discovery coefficients on a metagenome set that properly supersedes the 92,187. If unbinned α ≤ 0 in the habitats now cited at ≥ 0.5, the primary is dead.
2. Score the next examined tenth of the Mar del Plata harpacticoids. If novelty falls to the background rate of already-named species, the runner was a first-slice illusion and leaves RGC.
3. Kill any instance whose pipeline already publishes the remainder-channel α as a first-class estimand and treats α ≤ 0 as closure of *that* channel. The host-archaea control is the template.
4. Do not let a saturated genome channel retire the unbinned channel. That move is the queued False-Saturation Class. It needs its own session.
5. Controls must stay under 1. They did: 0.0196 and 0.0008.

## Adversarial review

| Temptation | Ruling |
|---|---|
| Mint 150 realm discoveries from the prompt's taxonomy | **Reject.** CLOSED-2026-09-30 and later. Rule 7 says the queued leftover is the session. |
| Re-issue DPC on the same *Nature Microbiology* paper | **Reject.** DPC owns denom privilege. RGC owns the derivative. Overlap penalized at 0.36, not zeroed. |
| Treat "every copepod was new" as a measured derivative | **Reject.** One slice. `derivative_measured=0.32`. Ranked second on purpose. |
| Invent a numerical α for MAGs | **Reject.** The paper gives floors and inequalities. `named_alpha_published=False` on those rows. |
| Call host-habitat archaeal saturation an RGC hit | **Reject.** Kill fired. Score 0.0196. |
| Call rarefaction the discovery | **Reject.** Control. Score 0.0008. Novelty cap 0.29. |
| Mint False-Saturation in this session | **Reject.** Different kill. Queued. |
| Use an unretrieved namesake as the type specimen | **Reject.** Type specimen is the retrieved 2026 *Nature Microbiology* paper. |
| Treat Ocean Census workshop names as Code descriptions | **Reject.** Identification rate only. |
| Claim a patent or a priority date | **Reject.** Timestamp is not filing. |

**What survives:** (1) On the 92,187-metagenome census, unbinned discovery stays unsaturated (α ≥ 0.5; hotspot habitats α ≥ 0.8) and the authors say it will keep outpacing genomes, so the discovered/discoverable gap widens; (2) the same paper's host-habitat archaeal genome channel is already saturated and scores ~0, so the kill has teeth; (3) the Mar del Plata copepod tenth is consistent with RGC and is not yet a derivative; (4) False-Saturation is the next leftover, not this one.

## Functions built this session

- `rgc_score` — 4 cases — primary 9.6657, runner 5.6886, controls 0.0196 and 0.0008
- `remainder_derivative` — 4 calls — two floor-only holds, one saturation kill, one false-saturation queue
- `single_bin_novelty` — 2 calls — copepods consistent-but-unmeasured; a fully examined empty-novelty drawer kills

## Selected sources

1. Prasoodanan et al., *Nature Microbiology* 11, 1437–1449 (2026). DOI 10.1038/s41564-026-02314-6. 92,187 metagenomes; ~705,000 bacterial and ~27,000 archaeal species-level clades; unbinned α ≥ 0.5 (hotspots ≥ 0.8); host-habitat archaeal genome discovery α ≤ 0; widening gap stated by the authors.
2. Nippon Foundation–Nekton Ocean Census, 1 Oct 2026. Mar del Plata Canyon workshop: 10% of harpacticoid samples examined; every specimen examined new to science; 20 species and 1 genus. https://oceancensus.org/press-release-57-new-marine-species-discovered-in-argentinas-submarine-canyons/
3. DPC-2026-10-07, sENZ5hFx/denominator-privilege-class-2026-10-07, which queued RGC and did not mint it. Skill rule 7.
4. Gotelli & Colwell rarefaction / species accumulation, as the method control, not as a 2026 census.
