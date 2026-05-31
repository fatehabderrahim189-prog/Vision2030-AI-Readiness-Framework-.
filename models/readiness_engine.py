"""
Readiness Engine — Vision 2030 AI Readiness Framework
Generates policy recommendations and trend projections.
"""

import numpy as np
from typing import List, Dict


class ReadinessEngine:
    """Core analytical engine for the V2030-ARF."""

    RECOMMENDATION_BANK = {
        "infrastructure": [
            {
                "title": "Accelerate National Broadband Expansion Program",
                "description": "Prioritize last-mile fiber connectivity to achieve 95%+ broadband "
                               "penetration. Implement public-private partnerships with major telecom "
                               "operators to reduce CAPEX barriers and accelerate rural coverage timelines "
                               "consistent with Vision 2030 smart cities objectives.",
                "priority": "HIGH",
            },
            {
                "title": "Establish National Cloud-First Government Policy",
                "description": "Mandate cloud migration for all public sector systems by 2027, leveraging "
                               "the national data center infrastructure. Negotiate sovereign cloud "
                               "agreements with hyperscalers (AWS, Azure, Google Cloud) to ensure "
                               "data residency compliance while benefiting from global AI tooling.",
                "priority": "HIGH",
            },
            {
                "title": "Launch AI Hardware Procurement Initiative",
                "description": "Establish a national GPU cluster program to democratize access to AI "
                               "compute for universities and startups, reducing the infrastructure cost "
                               "barrier to AI research and development by an estimated 60%.",
                "priority": "MEDIUM",
            },
        ],
        "talent": [
            {
                "title": "Create National AI Scholarship & Fellowship Program",
                "description": "Fund 5,000 annual AI and data science graduate scholarships at top "
                               "international universities, with a mandatory return-of-service commitment "
                               "to build a sovereign AI talent pool aligned with Vision 2030's "
                               "knowledge economy objectives.",
                "priority": "HIGH",
            },
            {
                "title": "Integrate AI Curriculum Across K-12 Education",
                "description": "Mandate computational thinking, data literacy, and AI fundamentals "
                               "in the national K-12 curriculum by 2026. Partner with platforms "
                               "like Coursera, edX, and local EdTech providers to deliver scalable "
                               "teacher training programs covering 50,000+ educators.",
                "priority": "HIGH",
            },
            {
                "title": "Establish AI Center of Excellence Network",
                "description": "Create 10 sector-specific AI Centers of Excellence co-located with "
                               "major universities and industry partners, targeting applied research "
                               "in healthcare AI, agricultural optimization, smart logistics, and "
                               "financial services automation.",
                "priority": "MEDIUM",
            },
        ],
        "governance": [
            {
                "title": "Enact Comprehensive National AI Strategy & Regulatory Framework",
                "description": "Develop and publish a National AI Strategy with legally binding "
                               "implementation milestones, ethics guidelines, liability frameworks, "
                               "and regulatory sandboxes. Model after Singapore's Model AI Governance "
                               "Framework and the EU AI Act risk-tiered approach.",
                "priority": "HIGH",
            },
            {
                "title": "Strengthen Data Protection & Privacy Legislation",
                "description": "Align national data protection law with GDPR-equivalent standards "
                               "to enable cross-border data flows and attract international AI investment. "
                               "Establish an independent Data Protection Authority with enforcement powers.",
                "priority": "HIGH",
            },
            {
                "title": "Launch Open Government Data Initiative",
                "description": "Mandate publication of non-sensitive government datasets on a "
                               "national open data portal with standardized APIs. Target 10,000+ "
                               "datasets across 12 ministries within 18 months, enabling private "
                               "sector AI application development on government data.",
                "priority": "MEDIUM",
            },
        ],
        "innovation": [
            {
                "title": "Create National AI Innovation Fund (500M+ USD)",
                "description": "Establish a sovereign AI innovation fund to co-invest in early-stage "
                               "AI startups, provide bridge funding for university spinoffs, and "
                               "support AI adoption grants for SMEs. Target 500+ funded companies "
                               "within 5 years to build a vibrant AI startup ecosystem.",
                "priority": "HIGH",
            },
            {
                "title": "Develop AI-Focused Special Economic Zones",
                "description": "Establish dedicated AI and DeepTech economic zones with preferential "
                               "tax treatment, streamlined business registration, and world-class "
                               "infrastructure. Model after Abu Dhabi's Hub71 and Singapore's "
                               "one-north ecosystem to attract global AI talent and capital.",
                "priority": "MEDIUM",
            },
            {
                "title": "Launch National AI Grand Challenges Program",
                "description": "Sponsor 5 annual AI Grand Challenges addressing national priorities "
                               "(healthcare, water, energy, logistics, education) with prize pools "
                               "of $1M+ per challenge. Grand Challenges accelerate applied AI "
                               "innovation and generate international visibility for the AI ecosystem.",
                "priority": "LOW",
            },
        ],
        "data": [
            {
                "title": "Build National Data Exchange Platform",
                "description": "Create a federated national data exchange platform enabling secure, "
                               "consent-based data sharing between government agencies, research "
                               "institutions, and the private sector. Implement differential privacy "
                               "and data clean room technologies to maximize data utility while "
                               "protecting individual privacy.",
                "priority": "HIGH",
            },
            {
                "title": "Launch National IoT Connectivity Program",
                "description": "Deploy a national IoT sensor network across critical infrastructure, "
                               "smart cities, and agricultural zones to generate real-time data "
                               "streams for AI applications in predictive maintenance, resource "
                               "optimization, and emergency response.",
                "priority": "MEDIUM",
            },
            {
                "title": "Establish AI-Ready Data Standards & Certification",
                "description": "Develop national data quality standards and certification processes "
                               "for AI training datasets. Incentivize data labeling industries and "
                               "create a national dataset repository for AI research aligned with "
                               "FAIR (Findable, Accessible, Interoperable, Reusable) data principles.",
                "priority": "MEDIUM",
            },
        ],
    }

    PILLAR_NAMES = {
        "infrastructure": "Digital Infrastructure",
        "talent": "Human Capital & Talent",
        "governance": "AI Governance & Policy",
        "innovation": "Innovation Ecosystem",
        "data": "Data Economy",
    }

    def __init__(self, weights: dict):
        self.weights = weights

    def generate_recommendations(
        self, pillar_scores: dict, country: str, top_n: int = 8
    ) -> List[Dict]:
        """
        Generate prioritized recommendations based on weakest pillars.

        Args:
            pillar_scores: dict of pillar scores
            country: country name
            top_n: max recommendations to return

        Returns:
            list of recommendation dicts
        """
        # Sort pillars by score ascending (weakest first)
        sorted_pillars = sorted(pillar_scores.items(), key=lambda x: x[1])

        recommendations = []
        for pillar_key, score in sorted_pillars:
            recs = self.RECOMMENDATION_BANK.get(pillar_key, [])
            # Elevate priority for very low scores
            for rec in recs[:2]:
                r = rec.copy()
                r["pillar"] = self.PILLAR_NAMES.get(pillar_key, pillar_key)
                if score < 40:
                    r["priority"] = "HIGH"
                elif score < 60:
                    r["priority"] = r["priority"] if r["priority"] == "HIGH" else "MEDIUM"
                recommendations.append(r)
            if len(recommendations) >= top_n:
                break

        # Sort by priority
        priority_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
        recommendations.sort(key=lambda x: priority_order.get(x["priority"], 3))
        return recommendations[:top_n]

    def generate_trend_data(self, country: str, years: list) -> dict:
        """
        Generate plausible historical trend data for a country.
        In production, this would fetch from World Bank / ITU API.

        Args:
            country: country name
            years: list of years

        Returns:
            dict of pillar -> list of scores
        """
        np.random.seed(hash(country) % 2**32)

        # Base values vary by country tier
        tier_map = {
            "Singapore": 85, "United States": 88, "South Korea": 82,
            "Germany": 79, "UAE": 74, "Malaysia": 58,
            "Saudi Arabia": 55, "Egypt": 44, "Morocco": 46, "Algeria": 36,
        }
        base = tier_map.get(country, 50)

        trend_data = {}
        pillars = ["Infrastructure", "Human Capital", "Governance", "Innovation", "Data Economy"]
        base_offsets = [-2, -5, 3, -8, -3]

        for pillar, offset in zip(pillars, base_offsets):
            pillar_base = max(10, min(95, base + offset))
            # Generate monotonically increasing trend with noise
            growth_rate = np.random.uniform(1.5, 4.5)
            n = len(years)
            values = []
            current = pillar_base - growth_rate * (n - 1)
            for i in range(n):
                noise = np.random.uniform(-1.5, 1.5)
                val = round(min(100, max(5, current + noise)), 1)
                values.append(val)
                current += growth_rate
            trend_data[pillar] = values

        return trend_data
