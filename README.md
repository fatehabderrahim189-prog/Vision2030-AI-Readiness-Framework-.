# 🌐 Vision 2030 AI Readiness Framework

![Streamlit App](https://img.shields.io/badge/Streamlit-App-red) ![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue) ![License: MIT](https://img.shields.io/badge/License-MIT-green) ![Research](https://img.shields.io/badge/Status-Research%20Prototype-orange)

**A Multi-Dimensional Assessment Model for Digital Economy Transformation**
Aligned with Saudi Vision 2030 · GCC Digital Agenda · UN SDG 9

---

## 📋 Abstract

The Vision 2030 AI Readiness Framework (V2030-ARF) is an open-source research prototype exploring how institutions and countries can be assessed for AI readiness across five weighted pillars.

| Pillar | Key Indicators |
|---|---|
| 🔌 Digital Infrastructure | Broadband penetration, cloud adoption, ICT investment |
| 🎓 Human Capital & Talent | STEM graduates, AI talent index, digital skills |
| ⚖️ AI Governance & Policy | Policy maturity, data protection, cybersecurity |
| 🚀 Innovation Ecosystem | R&D expenditure, startup density, patent applications |
| 📊 Data Economy | Open data availability, big data adoption, IoT deployment |

## 📌 A note on the data (read this first)

The 10-country dataset (`data/countries_data.py`, 250 indicator values) consists of **plausible estimates**, not values individually sourced, verified, or extracted from World Bank/WEF/ITU/Oxford Insights reports. The values were constructed to be directionally realistic (e.g. Singapore and the US score high, Algeria and Egypt score lower, consistent with general public knowledge of these countries' digital development), but **no individual figure traces to a specific cited report, page, or year.** The header comment referencing these organizations describes the general inspiration for the indicator categories, not a per-value data provenance.

**Treat every score in the dashboard as a demonstration of the scoring methodology on illustrative data — not as a real, defensible national AI-readiness ranking.** This is an important distinction for anyone citing this project: the *framework* (the weighting methodology, the five-pillar structure) is the research contribution; the *current numbers* are placeholders showing how that framework would work once populated with verified data. Building a real, cited data pipeline is the top item under Future Work below.

## 🎯 Research Objectives

1. Design a structured, reproducible AI readiness assessment framework.
2. Integrate multiple institutional dimensions into a unified, weighted evaluation model.
3. Develop an interpretable, adjustable scoring methodology.
4. Provide an open-source, interactive tool for policymakers and researchers to explore the methodology.

## 🚀 Live Demo

🌐 [Open Interactive Dashboard](https://qsxjdnqtcd5frcfsbl7wgz.streamlit.app/)

## 📊 Framework Architecture

```
V2030-ARF Score = Σ(wᵢ × Pᵢ), where Σwᵢ = 1.0, 0 ≤ Pᵢ ≤ 100
Pillar Score (Pᵢ) = Mean(normalized sub-indicators)
Default Weights: 0.20 per pillar (fully adjustable via dashboard)
```

**Pipeline:** Data Ingestion → Min-Max Normalization → Pillar Aggregation → Weighted Scoring → Visualization

## 🗂️ Repository Structure

This reflects what is actually in the repository (not an aspirational structure):

```
Vision2030-AI-Readiness-Framework-/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── Vision_2030_AI_Readiness_Framework...pdf   # Technical report (v1.0)
│
├── models/
│   ├── __init__.py
│   ├── scoring.py               # Composite index computation
│   └── readiness_engine.py      # Recommendations & trend engine
│
├── data/
│   ├── __init__.py
│   └── countries_data.py        # 10-country illustrative dataset — see data note above
│
└── .github/workflows/           # CI configuration
```

## ⚙️ Installation & Local Setup

```bash
git clone https://github.com/fatehabderrahim189-prog/Vision2030-AI-Readiness-Framework-.git
cd Vision2030-AI-Readiness-Framework-

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```
App opens at `http://localhost:8501`.

## 🌍 Countries Included (v1.0)

Saudi Arabia · UAE · Singapore · South Korea · Germany · United States · Malaysia · Egypt · Morocco · Algeria

## 📈 Key Features

- Interactive radar charts — pillar-by-pillar readiness profiles
- Global comparison heatmaps across the 10 included countries
- Adjustable pillar weights for sensitivity analysis
- Auto-generated policy recommendations based on the configured weights
- Embedded technical report

## 📄 Technical Report

The full technical report (methodology, limitations, references) is included in the repository as a PDF: `Vision_2030_AI_Readiness_Framework___Institutional_AI_Readiness_Assessment_Platform (1).pdf`.

**Citation (APA):**
```
Boukhalfa, F. A. (2026). Vision 2030 AI Readiness Framework: A Multi-Dimensional
Assessment Model for Digital Economy Transformation in Emerging Economies.
USTHB, Algiers, Algeria. GitHub: https://github.com/fatehabderrahim189-prog/Vision2030-AI-Readiness-Framework-
```

## Limitations

- The dataset is illustrative/estimated, not individually sourced or verified per indicator (see data note above). Composite scores are a methodology demonstration, not a validated ranking.
- The model relies on static, manually-constructed indicators rather than a live, cited data pipeline.
- It is a diagnostic/exploratory tool, not a certified assessment instrument.

## 🔭 Future Work

- Integrate a live, cited data pipeline (World Bank / WEF / ITU APIs) with per-indicator source links
- Independently re-verify current dataset values against primary sources
- Validate the weighting methodology against expert or institutional feedback
- Arabic-language interface

## 👤 Author

**Fateh Abderrahim Boukhalfa**
Engineering student, University of Sciences and Technology Houari Boumediene (USTHB), Algiers, Algeria
📧 fatehabderrahim189@gmail.com

## 📜 License

MIT License — see `LICENSE`.

## 🤝 Contributing

Contributions welcome — please open an issue or pull request. Areas of interest: live data integration, additional countries, predictive modeling, Arabic interface.

