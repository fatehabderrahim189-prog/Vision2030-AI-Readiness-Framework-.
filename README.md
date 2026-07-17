# 🌐 Vision 2030 AI Readiness Framework

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Research](https://img.shields.io/badge/Research-MIS%20%7C%20AI%20Strategy-orange.svg)](#)
[![Vision 2030](https://img.shields.io/badge/Aligned-Saudi%20Vision%202030-006c35.svg)](#)

**A Multi-Dimensional Assessment Model for Digital Economy Transformation**  
*Aligned with Saudi Vision 2030 · GCC Digital Agenda · UN SDG 9*

</div>

---

## 📋 Abstract

The **Vision 2030 AI Readiness Framework (V2030-ARF)** is an open-source, multi-dimensional assessment model designed to evaluate and benchmark national artificial intelligence readiness levels against the strategic objectives of Saudi Vision 2030 and broader GCC digital transformation agendas.

The framework synthesizes **five core pillars** into a weighted composite readiness index:

| Pillar | Key Indicators |
|--------|---------------|
| 🔌 Digital Infrastructure | Broadband penetration, cloud adoption, ICT investment |
| 🎓 Human Capital & Talent | STEM graduates, AI talent index, digital skills |
| ⚖️ AI Governance & Policy | Policy maturity, data protection, cybersecurity |
| 🚀 Innovation Ecosystem | R&D expenditure, startup density, patent applications |
| 📊 Data Economy | Open data availability, big data adoption, IoT deployment |

---

## 🎯 Research Objectives

1. Develop a reproducible, open-source AI readiness index aligned with Vision 2030 KPIs
2. Enable cross-national comparison across 10+ countries using World Bank, WEF, and ITU data
3. Generate evidence-based policy recommendations for bridging the AI readiness gap
4. Provide an interactive tool for policymakers, researchers, and development organizations

---

## 🚀 Live Demo

> **[🌐 Open Interactive Dashboard →]
> https://qsxjdnqtcd5frcfsbl7wgz.streamlit.app/

---

## 📊 Framework Architecture

```
V2030-ARF Score = Σ(wᵢ × Pᵢ), where Σwᵢ = 1.0, 0 ≤ Pᵢ ≤ 100

Pillar Score (Pᵢ) = Mean(normalized sub-indicators)
Default Weights: 0.20 per pillar (fully adjustable via dashboard)
```

### Sub-Indicator Sources
- **World Bank** — World Development Indicators (WDI)
- **World Economic Forum** — Global Competitiveness Report 2023
- **ITU** — ICT Development Index 2023
- **Oxford Insights** — Government AI Readiness Index 2023
- **OECD** — AI Policy Observatory

---

## 🗂️ Project Structure

```
Vision2030-AI-Readiness-Framework/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── models/
│   ├── __init__.py
│   ├── scoring.py              # Composite index computation
│   └── readiness_engine.py     # Recommendations & trend engine
│
├── data/
│   ├── __init__.py
│   └── countries_data.py       # 10-country normalized dataset
│
├── research/
│   └── V2030_ARF_Research_Paper.md   # Full academic paper
│
└── assets/
    └── screenshots/            # Dashboard screenshots
```

---

## ⚙️ Installation & Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Vision2030-AI-Readiness-Framework.git
cd Vision2030-AI-Readiness-Framework

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run app.py
```

App will open at `http://localhost:8501`

---

## 🌍 Countries Included (v1.0)

Saudi Arabia · UAE · Singapore · South Korea · Germany · United States · Malaysia · Egypt · Morocco · Algeria

---

## 📈 Key Features

- **Interactive Radar Charts** — Visualize pillar-by-pillar readiness profiles
- **Global Comparison Heatmaps** — Cross-national benchmarking across 10 nations
- **AI-Generated Policy Recommendations** — Prioritized by gap severity
- **Implementation Roadmaps** — Projected score improvements over 5-year horizons
- **Adjustable Pillar Weights** — Sensitivity analysis for different policy priorities
- **Embedded Research Report** — Full academic paper with Literature Review, Methodology, Results

---

## 📄 Research Paper

The full academic paper is available in [`research/V2030_ARF_Research_Paper.md`](research/V2030_ARF_Research_Paper.md).

**Citation (APA):**
```
Boukhalfa, F. A. (2026). Vision 2030 AI Readiness Framework: A Multi-Dimensional 
Assessment Model for Digital Economy Transformation in Emerging Economies. 
USTHB, Algiers, Algeria. GitHub: https://github.com/YOUR_USERNAME/Vision2030-AI-Readiness-Framework
```

---

## 👤 Author

**Fateh Abderrahim Boukhalfa**  
First-Year STEM Student | University of Sciences and Technology Houari Boumediene (USTHB)  
Algiers, Algeria

- 📧 fatehabderrahim189@gmail.com  
- 🎓 PSAT 1520/1520 (Top 1% Globally)  
- 🌐 C1-C2 English Proficiency (EF Certified)  
- 📜 11+ International Certifications (HP LIFE · HubSpot · IBM SkillsBuild)  
- 🔬 Research Interests: MIS · AI Strategy · Digital Transformation · Vision 2030

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a pull request.

Areas for contribution:
- Adding more countries to the dataset
- Integrating live World Bank API feeds
- Machine learning-based predictive modeling
- Arabic language interface

---

<div align="center">
<strong>⭐ Star this repository if you find it useful for your research!</strong>
</div>
