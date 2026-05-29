"""Generate specific-human-error-modes.svg for the blog post.

Two-panel bar chart: h-error-pos and h-trunc-pos match rates with Wilson 95% CIs
on the underlying proportions. Three methods per panel: HUMAN (ceiling), HistGBT
(heuristic), COMPACTOR + Qwen3-8B (published).

Style: serif (Palatino / et-book-ish), muted earth-tones, no top/right spines,
no gridlines; matches the Tufte / latex.css feel of the surrounding page.

Output: figures/specific-human-error-modes.svg (vector; scales cleanly inline).

Run from the repo root:
    python blog/figures/specific-human-error-modes.py

Counts are hard-coded with citations to the experiment dir they came from.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------------------------
# Numbers — from experiments/audit/predict_human_digit/results_ensemble.json
# (HistGBT) and experiments/audit/compactor_on_human_golds/runs/*.jsonl
# (COMPACTOR rows; per-TEST-split re-aggregation in the README).
#
# Format: dict per method with hits + n for each of the 4 metric subsets.
# Qwen3-8B + COMPACTOR has smaller denominators on overall and h-correct
# because 15 of 119 TEST trials dropped due to OpenRouter route instability.
# ---------------------------------------------------------------------------

DATA = [
    # (label, overall_hits, overall_n, hcorrect_hits, hcorrect_n,
    #         herror_hits, herror_n, htrunc_hits, htrunc_n)
    ("HUMAN (self)",              517, 517, 465, 465, 52, 52, 15, 15),
    ("HistGBT",                   467, 517, 460, 465,  7, 52,  4, 15),
    ("Qwen3-next-80B + COMPACTOR", 426, 517, 422, 465,  4, 52,  1, 15),
]

PANELS = [
    # (panel_title, data_index_for_hits, data_index_for_n)
    ("overall (n=517)",                                    1, 2),
    ("h-correct-pos (n=465)\nhuman typed gold",            3, 4),
    ("h-error-pos (n=52)\nhuman typed wrong digit",        5, 6),
    ("h-trunc-pos (n=15)\nhuman stopped early",            7, 8),
]

# Warm earth-tone palette inspired by Will Brown's recent blog post styling:
# warm taupe-brown for the human ceiling, sage-teal for the heuristic,
# warm orange for the published method.
COLORS = {
    "HUMAN (self)":                "#3C0008",
    "HistGBT":                     "#5e9e94",
    "Qwen3-next-80B + COMPACTOR":  "#d8814f",
}

BAR_ALPHA = 0.85


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float, float]:
    """Returns (point, lo, hi) Wilson interval on k/n at confidence z."""
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    p = k / n
    denom = 1.0 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1.0 - p) / n + z * z / (4 * n * n)) / denom
    return p, max(0.0, center - half), min(1.0, center + half)


def make_figure(out_path: Path) -> None:
    # Four panels side-by-side: overall, h-correct, h-error, h-trunc.
    fig, axes = plt.subplots(1, 4, figsize=(15.2, 4.6), constrained_layout=True)

    labels = [r[0] for r in DATA]
    x = np.arange(len(labels))

    for ax, (panel_title, hit_idx, n_idx) in zip(axes, PANELS):
        rates, los, his, hits, ns = [], [], [], [], []
        for r in DATA:
            k = r[hit_idx]; n = r[n_idx]
            p, lo, hi = wilson_ci(k, n)
            rates.append(p)
            los.append(max(0.0, p - lo))
            his.append(max(0.0, hi - p))
            hits.append(k); ns.append(n)

        colors = [COLORS[l] for l in labels]
        ax.bar(x, rates, color=colors, alpha=BAR_ALPHA, width=0.66,
               edgecolor="none", zorder=2)
        ax.errorbar(x, rates, yerr=[los, his], fmt="none", ecolor="#111",
                    capsize=7, capthick=1.6, elinewidth=1.6, zorder=3)

        for xi, (k, n, p, hi) in enumerate(zip(hits, ns, rates, his)):
            ax.text(xi, p + hi + 0.03,
                    f"{k}/{n}\n{p*100:.1f}%",
                    ha="center", va="bottom",
                    fontsize=9.0, color="#222")

        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=9.5, rotation=15, ha="right")
        ax.set_ylim(0, 1.20)
        ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels([f"{int(t*100)}%" for t in
                            [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]],
                           fontsize=9.5)
        ax.set_title(panel_title, fontsize=10.5, color="#111", pad=10)

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#444")
        ax.spines["bottom"].set_color("#444")
        ax.tick_params(axis="x", length=0, pad=6, colors="#222")
        ax.tick_params(axis="y", length=3, colors="#222")
        ax.set_axisbelow(True)

    fig.suptitle(
        "Per-position match against held-out humans on digit-span forward TEST split",
        fontsize=12.5, color="#111", y=1.04,
    )

    # Use a serif family that looks at home in the Tufte / et-book layout.
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = [
        "Palatino", "Palatino Linotype", "Book Antiqua", "Georgia",
        "DejaVu Serif", "serif",
    ]
    plt.rcParams["axes.titleweight"] = "normal"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, format="svg", bbox_inches="tight", transparent=True)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    out = Path(__file__).parent / "specific-human-error-modes.svg"
    make_figure(out)
