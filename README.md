# Remainder-Growth Class (RGC)

**Timestamp:** Friday, 9 October 2026, 13:40 EDT / `2026-10-09T17:40:00Z`
**Session ID:** `20261009-1340-rgc`
**Author:** Haley Ann Bird · GitHub `sENZ5hFx`
**Status:** Research-stage classification of a knowledge gap. **Not** a physical discovery, law, patent, or proof.

Full record: [SESSION.md](./SESSION.md)

## Primary insight

Added observational effort grows the unnamed remainder faster than the named set. The kill is saturation: if the remainder channel's discovery coefficient is already ≤ 0, the instance leaves the class.

This is the leftover queued on 2026-10-07 by Denominator-Privilege Class and not given a Discovery ID. DPC owns the privilege of a construct denominator. RGC owns the derivative. False-Saturation Class is queued, not minted.

## Rank (controls excluded)

| Rank | Score | ID | Realm | Status |
|---:|---:|---|---|---|
| 1 | 9.6657 | unbinned_widening_gap | land | confirmed |
| 2 | 5.6886 | mar_del_plata_copepods | ocean | unsolved |

Negative controls (host-habitat archaeal genomes already saturated; textbook rarefaction plateau) scored 0.0196 and 0.0008. `controls_ok = true`.

## Kill rule

Remainder channel saturated (`α ≤ 0`, or a nested rarefaction slope at ~0). A one-time novelty rate is not a measured derivative and must not outrank one.

## Repo contents

- `SESSION.md` — realm coverage as instances of this class, not 150 mints
- `session_log.json` — session schema
- `rgc_result.json` — scorer output, SHA-256 in `SHA256.txt`
- `rgc_score.py` — `rgc_score`, `remainder_derivative`, `single_bin_novelty`
- `skills/` — high-agency-partner, skill-creator, remainder-growth-class

## Notion

Row in Haley's IP-Secured Discoveries Log. IP Readiness = Logged. Not PPA Ready. Not Filed.

© 2026 Haley Ann Bird — original expression only. Underlying natural facts remain public.

## Current evaluator amendment (2026-11-12, draft)

The original `rgc_result.json` and `SHA256.txt` are retained as **dated historical output**, including their earlier boolean floor-only verdicts. They are not re-labeled as source evidence or silently overwritten.

An unnamed-channel coefficient by itself cannot prove that the unnamed channel *outruns* a named channel. The revised `remainder_derivative` returns `rgc_holds: null` for absent or unpublished named coefficients. An illustrative unverified plateau can be marked `hypothetical_false_saturation`, not a verified queue. A verified saturation kill still returns false, and explicitly published paired coefficients can support a positive/negative comparison in this software heuristic.

To regenerate **current** results without touching historical snapshots: `python3 rgc_score.py` now writes `rgc_result_current.json` and `SHA256_current.txt` next to the source. Run zero-dependency regressions with `python3 -m unittest -v test_rgc_evidence.py`.

These checks validate software logic only. They do not establish literature provenance, physical discovery, peer review, or patent status.
