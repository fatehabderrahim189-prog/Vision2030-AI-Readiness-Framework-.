"""
Scoring Module — Vision 2030 AI Readiness Framework
Computes pillar scores and composite index.
"""

import numpy as np


def _pillar_mean(indicators: dict) -> float:
    """Compute unweighted mean of a pillar's sub-indicators."""
    vals = list(indicators.values())
    return float(np.mean(vals)) if vals else 0.0


def get_pillar_scores(country_data: dict, weights: dict) -> dict:
    """
    Compute normalized pillar scores (0-100) for a country.

    Args:
        country_data: dict with keys matching pillar names
        weights: dict of pillar weights (used only for validation)

    Returns:
        dict of pillar_name -> float score
    """
    pillar_map = {
        "infrastructure": "infrastructure",
        "talent": "talent",
        "governance": "governance",
        "innovation": "innovation",
        "data": "data",
    }

    scores = {}
    for key, data_key in pillar_map.items():
        if data_key in country_data:
            scores[key] = round(_pillar_mean(country_data[data_key]), 2)
        else:
            scores[key] = 0.0

    return scores


def compute_composite_score(pillar_scores: dict, weights: dict) -> float:
    """
    Compute weighted composite AI readiness score.

    Args:
        pillar_scores: dict of pillar_name -> float score
        weights: dict of pillar_name -> float weight

    Returns:
        float: composite score 0-100
    """
    total_weight = sum(weights.values())
    if total_weight == 0:
        return 0.0

    composite = sum(
        pillar_scores.get(pillar, 0) * weight
        for pillar, weight in weights.items()
    )
    # Normalize by actual total weight (handles non-unity sums)
    composite = composite / total_weight
    return round(min(max(composite, 0), 100), 2)
