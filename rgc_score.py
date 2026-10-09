#!/usr/bin/env python3
"""Remainder-Growth Class (RGC) scorer — 2026-10-09.

Research-stage classification. Not a physical discovery, not peer review,
not a patent. Scores whether added observational effort grows the unnamed
remainder faster than the named set.

Score:
    40 * outruns * unsaturated * derivative_measured * evidence
      * (1 - spoken) * (1 - prior_overlap)

Kill: saturation. If the remainder channel's discovery coefficient
alpha <= 0, or a nested rarefaction slope is ~0, the instance leaves RGC.
A coarse channel plateauing while a finer channel still climbs is NOT a
kill of RGC; that false close is queued as False-Saturation Class and is
not minted here.

DPC (2026-10-07) owns the privilege of a construct denominator.
RGC owns the derivative. Same paper can feed both; the factors differ.

Author: Haley Ann Bird / autonomous Grok agent
Session: 2026-10-09T17:40:00Z
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PRIOR_CLASSES = (
    "Dark Biosphere",
    "TAC",
    "Cadence Mismatch",
    "NCR",
    "FAC",
    "CIC",
    "JAC",
    "IOA",
    "DIC",
    "PPC",
    "UCC",
    "DCC",
    "FCC",
    "OAC",
    "UPRC",
    "CIP",
    "TPC",
    "CMC",
    "EFC",
    "IPC",
    "SBC",
    "IRC",
    "SEC",
    "RJC",
    "ANC",
    "UEDP",
    "FPC",
    "PDC",
    "DPC",
    "RD Plane-Split",
    "CHL",
    "CLOSED-2026-09-30",
    "CLOSED-2026-10-02",
    "CLOSED-2026-10-04",
    "CLOSED-2026-10-05",
    "CLOSED-2026-10-07",
)

# DPC owns denom privilege. FCC owns frontier coincidence, not d(remainder)/d(effort).
OVERLAP_OWNERS = ("DPC", "FCC", "DCC", "OAC", "FPC")


def _unit(name: str, value: float) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"{name} must be a real number, got {type(value).__name__}")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    if value < 0.0 or value > 1.0:
        raise ValueError(f"{name} must be in [0, 1], got {value}")
    return float(value)


@dataclass
class RgcCase:
    id: str
    realm: str
    quantity: str
    named_object: str
    remainder_object: str
    outruns: float
    unsaturated: float
    derivative_measured: float
    evidence: float
    spoken: float
    prior_overlap: float
    status: str
    source: str
    role: str = "candidate"
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.id or not self.id.replace("_", "").isalnum():
            raise ValueError(f"id must be snake_case alphanumeric, got {self.id!r}")
        if not self.realm.strip():
            raise ValueError("realm is required")
        if not self.named_object.strip() or not self.remainder_object.strip():
            raise ValueError(f"{self.id}: named_object and remainder_object required")
        self.outruns = _unit("outruns", self.outruns)
        self.unsaturated = _unit("unsaturated", self.unsaturated)
        self.derivative_measured = _unit("derivative_measured", self.derivative_measured)
        self.evidence = _unit("evidence", self.evidence)
        self.spoken = _unit("spoken", self.spoken)
        self.prior_overlap = _unit("prior_overlap", self.prior_overlap)
        allowed = {
            "confirmed",
            "disputed",
            "unsolved",
            "competing",
            "retired",
            "control",
        }
        if self.status not in allowed:
            raise ValueError(f"status must be one of {sorted(allowed)}")


def rgc_score(case: RgcCase) -> dict[str, Any]:
    """Score one RGC instance.

    Added effort grows the unnamed remainder faster than the named set.
    Controls (saturated remainder channel, or the textbook rarefaction
    namesake) must land near zero.
    """
    keep = (
        40.0
        * case.outruns
        * case.unsaturated
        * case.derivative_measured
        * case.evidence
        * (1.0 - case.spoken)
        * (1.0 - case.prior_overlap)
    )
    if case.status in {"retired", "control"}:
        ruling = "control_or_retired"
    elif keep < 1.0:
        ruling = "below_threshold"
    elif case.prior_overlap >= 0.60:
        ruling = "overlap_penalty"
    else:
        ruling = "keep"

    return {
        "id": case.id,
        "realm": case.realm,
        "quantity": case.quantity,
        "named_object": case.named_object,
        "remainder_object": case.remainder_object,
        "score": round(keep, 4),
        "ruling": ruling,
        "role": case.role,
        "status": case.status,
        "factors": {
            "outruns": case.outruns,
            "unsaturated": case.unsaturated,
            "derivative_measured": case.derivative_measured,
            "evidence": case.evidence,
            "spoken": case.spoken,
            "prior_overlap": case.prior_overlap,
            "unspoken": round(1.0 - case.spoken, 4),
            "novelty_vs_archive": round(1.0 - case.prior_overlap, 4),
        },
        "source": case.source,
        "notes": case.notes,
    }


def remainder_derivative(
    case_id: str,
    alpha_remainder: float,
    alpha_named: float | None,
    *,
    named_alpha_published: bool,
) -> dict[str, Any]:
    """Compare discovery coefficients.

    alpha <= 0: saturated (additional samples add nothing on that channel).
    alpha in (0, 1]: unsaturated. Pass alpha_named=None when the source
    states only that the named channel is outpaced, without a point value.
    Do not invent that point value.

    Kill: alpha_remainder <= 0.
    If the named channel is saturated and the remainder channel is not,
    RGC still holds; the coarse-plateau misreading is queued False-Saturation.
    """
    if not case_id:
        raise ValueError("case_id required")

    def _alpha(name: str, value: float | None) -> float | None:
        if value is None:
            return None
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"{name} must be a real number or None")
        if not math.isfinite(value):
            raise ValueError(f"{name} must be finite")
        if value < -0.05 or value > 1.05:
            raise ValueError(f"{name} outside a discovery-coefficient range: {value}")
        return float(value)

    alpha_remainder = _alpha("alpha_remainder", alpha_remainder)
    alpha_named = _alpha("alpha_named", alpha_named)
    if alpha_remainder is None:
        raise ValueError("alpha_remainder is required")
    if named_alpha_published and alpha_named is None:
        raise ValueError("named_alpha_published requires alpha_named")

    if alpha_remainder <= 0.0:
        mode = "saturated_kill"
        rgc_holds = False
        gap = None if alpha_named is None else round(alpha_remainder - alpha_named, 4)
    elif alpha_named is None:
        mode = "remainder_floor_only"
        rgc_holds = alpha_remainder >= 0.5
        gap = None
    else:
        gap_raw = alpha_remainder - alpha_named
        gap = round(gap_raw, 4)
        if gap_raw <= 0.0:
            mode = "named_keeps_pace"
            rgc_holds = False
        elif gap_raw >= 0.15 and alpha_remainder >= 0.5:
            mode = "remainder_outruns"
            rgc_holds = True
        else:
            mode = "weak_outrun"
            rgc_holds = True

    queued = bool(
        alpha_named is not None and alpha_named <= 0.0 and alpha_remainder > 0.2
    )
    return {
        "id": case_id,
        "alpha_remainder": alpha_remainder,
        "alpha_named": alpha_named,
        "named_alpha_published": named_alpha_published,
        "alpha_gap": gap,
        "mode": mode,
        "rgc_holds": rgc_holds,
        "kill_rule_fired": mode == "saturated_kill",
        "queued_false_saturation": queued,
        "note": (
            None
            if named_alpha_published or alpha_named is not None
            else "No published point estimate for alpha_named. Floor of the remainder channel only."
        ),
    }


def single_bin_novelty(
    case_id: str,
    examined_fraction: float,
    novelty_rate: float,
) -> dict[str, Any]:
    """A single examined slice that is almost entirely unnamed.

    This is NOT a measured derivative across effort. It can support RGC only
    as a prediction about the unexamined stock. derivative_measured must stay
    low in the scorer. If examined_fraction is already ~1 and novelty_rate ~0,
    the bin is a saturated census, and the kill fires.
    """
    examined_fraction = _unit("examined_fraction", examined_fraction)
    novelty_rate = _unit("novelty_rate", novelty_rate)
    unexamined = 1.0 - examined_fraction
    if examined_fraction >= 0.90 and novelty_rate <= 0.05:
        mode = "saturated_kill"
        rgc_holds = False
    elif novelty_rate >= 0.80 and unexamined >= 0.50:
        mode = "single_bin_consistent"
        rgc_holds = True
    else:
        mode = "inconclusive"
        rgc_holds = False
    return {
        "id": case_id,
        "examined_fraction": examined_fraction,
        "novelty_rate": novelty_rate,
        "unexamined_fraction": round(unexamined, 4),
        "mode": mode,
        "rgc_holds": rgc_holds,
        "derivative_measured": False,
        "kill_rule_fired": mode == "saturated_kill",
        "note": "One slice is not d(remainder)/d(effort). Do not outrank a measured alpha gap.",
    }


CASES: list[RgcCase] = [
    RgcCase(
        id="unbinned_widening_gap",
        realm="land",
        quantity="discoverable vs genomically represented prokaryotic species",
        named_object="isolate genomes and MAGs (17.8% of bacterial species-level diversity; 24.6% of archaeal)",
        remainder_object="species-level clades hidden in unbinned contigs (~705,000 bacterial; ~27,000 archaeal)",
        outruns=0.92,
        unsaturated=0.90,
        derivative_measured=0.95,
        evidence=0.96,
        spoken=0.50,
        prior_overlap=0.36,
        status="confirmed",
        source=(
            "Prasoodanan, Maistrenko, Fullam, Mende, Kartal, Coelho, Spang, Bork & Schmidt, "
            "Nature Microbiology 11, 1437–1449 (2026). DOI 10.1038/s41564-026-02314-6. "
            "92,187 metagenomes; 502 million marker-gene sequences. "
            "Unbinned discovery outpaces MAG discovery (alpha >= 0.5 across most habitats; "
            "soils, wetlands, rhizosphere, freshwater, non-mammalian guts alpha >= 0.8). "
            "Authors: the gap between discovered and discoverable 'will continue to widen.'"
        ),
        role="primary",
        notes=(
            "DPC already owns treating the discoverable set as the 'all microbes' denominator. "
            "RGC owns the derivative: marginal samples add unbinned species faster than they add "
            "genomes. Spoken as a result inside this paper (0.50), not as a cross-realm class. "
            "10 undescribed archaeal and 145 undescribed bacterial phyla are a stock, not the derivative."
        ),
    ),
    RgcCase(
        id="mar_del_plata_copepods",
        realm="ocean",
        quantity="harpacticoid copepods from Mar del Plata Canyon, workshop identifications",
        named_object="20 copepod species plus 1 genus identified from the examined tenth",
        remainder_object="the unexamined 90% of the collected harpacticoid samples",
        outruns=0.94,
        unsaturated=0.88,
        derivative_measured=0.32,
        evidence=0.84,
        spoken=0.22,
        prior_overlap=0.18,
        status="unsolved",
        source=(
            "Nippon Foundation–Nekton Ocean Census press release, 1 Oct 2026, "
            "https://oceancensus.org/press-release-57-new-marine-species-discovered-in-argentinas-submarine-canyons/ . "
            "Workshop 13–24 July 2026, Universidad Maimónides, Buenos Aires, on Schmidt Ocean Institute "
            "Falkor (too) samples from the July–August 2025 Mar del Plata Canyon expedition. "
            "Quote: examined just 10% of collected copepod samples; every specimen examined was a species "
            "new to science; 20 new species and 1 new genus. Workshop total 57 species and 5 genera."
        ),
        role="runner",
        notes=(
            "single_bin_novelty only. The derivative across the remaining 90% has not been measured. "
            "Workshop identification is not a Code-published description. Not a stock-status finding "
            "and not proof that the next tenth will also be 100% new. Ranked below the measured alpha gap."
        ),
    ),
    RgcCase(
        id="archaea_host_genome_saturated",
        realm="land",
        quantity="metagenomic representation of archaea already in reference genome sets, host habitats",
        named_object="archaeal species in proGenomes3 and GTDB r220 recoverable by current metagenomic approaches",
        remainder_object="additional archaeal species those approaches would add in infant gut, oral, skin",
        outruns=0.06,
        unsaturated=0.04,
        derivative_measured=0.90,
        evidence=0.92,
        spoken=0.72,
        prior_overlap=0.12,
        status="control",
        source=(
            "Same paper, Nature Microbiology 11, 1437–1449 (2026). Genome-based archaeal discovery "
            "fully saturated (alpha <= 0) or approaching saturation in most host-associated and "
            "anthropogenic habitats. Adding more samples is not expected to increase metagenomic "
            "representation of that reference-recoverable set in human infant gut, oral, or skin."
        ),
        role="control",
        notes=(
            "Must score near zero. Saturation of this channel fires the kill. "
            "Do not confuse it with unbinned alpha, which the same paper says stays higher — "
            "that misreading is queued False-Saturation, not an RGC hit."
        ),
    ),
    RgcCase(
        id="rarefaction_plateau_namesake",
        realm="humans",
        quantity="textbook species-accumulation curve that has reached a plateau",
        named_object="species already on a saturated accumulation curve",
        remainder_object="expected new species at the terminal sample (slope ~ 0)",
        outruns=0.04,
        unsaturated=0.03,
        derivative_measured=0.80,
        evidence=0.70,
        spoken=0.97,
        prior_overlap=0.05,
        status="control",
        source=(
            "Gotelli & Colwell, and the standard rarefaction / Chao asymptote machinery. "
            "Method namesake retrieved as the kill definition, not as a 2026 census. "
            "A flat terminal slope is the kill, not an instance."
        ),
        role="control",
        notes="Must score near zero. RGC is not the rediscovery of rarefaction.",
    ),
]


def rank_cases(cases: list[RgcCase] | None = None) -> dict[str, Any]:
    cases = cases or CASES
    rows = [rgc_score(c) for c in cases]
    rows.sort(key=lambda r: (-r["score"], r["id"]))
    keepers = [r for r in rows if r["ruling"] == "keep"]
    controls = [r for r in rows if r["role"] == "control"]
    return {
        "class": "Remainder-Growth Class (RGC)",
        "discovery_id": "RGC-2026-10-09",
        "session": "2026-10-09T17:40:00Z",
        "formula": (
            "40 * outruns * unsaturated * derivative_measured * evidence "
            "* (1-spoken) * (1-prior_overlap)"
        ),
        "kill_rule": (
            "If the remainder channel is saturated (discovery coefficient alpha <= 0, "
            "or a nested rarefaction slope ~ 0), the instance leaves RGC."
        ),
        "not_owned": (
            "DPC owns denom privilege. FCC owns which frontiers coincide. "
            "False-Saturation (coarse alpha <= 0 reported as census closure while a finer "
            "channel still climbs) is queued, not minted."
        ),
        "archive_subtracted": list(PRIOR_CLASSES),
        "overlap_owners": list(OVERLAP_OWNERS),
        "n_cases": len(rows),
        "n_keep": len(keepers),
        "ranking": rows,
        "primary": next((r for r in rows if r["role"] == "primary"), None),
        "controls_ok": all(r["score"] < 1.0 for r in controls),
        "novelty_capped": 0.29,
        "coherence": 0.80,
        "legal": (
            "Research-stage classification. Not a physical discovery, not peer review, "
            "not a patent. Timestamp is not filing."
        ),
    }


def run() -> dict[str, Any]:
    ranked = rank_cases()
    derivatives = [
        # Published floors only. Do not invent a point estimate for alpha_named.
        remainder_derivative(
            "unbinned_vs_mag_floor", 0.50, None, named_alpha_published=False
        ),
        remainder_derivative(
            "soil_hotspot_floor", 0.80, None, named_alpha_published=False
        ),
        remainder_derivative(
            "archaea_host_genome_saturated", 0.00, 0.00, named_alpha_published=True
        ),
        # Illustrative queue only: coarse channel at the kill boundary, fine channel
        # still at the paper's unbinned floor. Not a second empirical alpha pair.
        remainder_derivative(
            "false_saturation_queue", 0.50, 0.00, named_alpha_published=False
        ),
    ]
    bins = [
        single_bin_novelty("mar_del_plata_copepods", 0.10, 1.00),
        single_bin_novelty("saturated_drawer_control", 1.00, 0.00),
    ]
    if not ranked["controls_ok"]:
        raise SystemExit("controls failed: a control scored >= 1")
    primary = ranked["primary"]
    if primary is None or primary["id"] != "unbinned_widening_gap":
        raise SystemExit(f"primary moved: {primary}")
    if primary["score"] <= ranked["ranking"][-1]["score"]:
        raise SystemExit("ranking degenerate")
    # The single-bin copepod case must not outrank the measured alpha gap.
    by_id = {r["id"]: r for r in ranked["ranking"]}
    if by_id["mar_del_plata_copepods"]["score"] >= by_id["unbinned_widening_gap"]["score"]:
        raise SystemExit("single-bin novelty outranked the measured derivative")
    for c in ranked["ranking"]:
        if c["role"] == "control" and c["score"] >= 1.0:
            raise SystemExit(f"control {c['id']} scored {c['score']}")
    false_sat = next(d for d in derivatives if d["id"] == "false_saturation_queue")
    if not false_sat["queued_false_saturation"] or not false_sat["rgc_holds"]:
        raise SystemExit("false-saturation queue failed")
    sat = next(d for d in derivatives if d["id"] == "archaea_host_genome_saturated")
    if not sat["kill_rule_fired"]:
        raise SystemExit("saturation kill did not fire")
    return {
        "ranked": ranked,
        "derivatives": derivatives,
        "single_bins": bins,
        "iteration": {
            "new_gap": (
                "False-Saturation Class: a coarse channel with alpha <= 0 is reported "
                "as the census closing, while a finer channel's alpha stays high. "
                "Kill would differ (the finer channel is already inside the same likelihood). "
                "Queued. Not minted."
            ),
            "minted": False,
        },
    }


def main() -> None:
    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    out = Path(__file__).with_name("rgc_result.json")
    out.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    Path(__file__).with_name("SHA256.txt").write_text(digest + "\n", encoding="utf-8")
    print(digest)
    for row in payload["ranked"]["ranking"]:
        print(f"{row['score']:8.4f}  {row['ruling']:22}  {row['id']}")
    print("controls_ok", payload["ranked"]["controls_ok"])


if __name__ == "__main__":
    main()
