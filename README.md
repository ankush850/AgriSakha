# AgriSakha AI - Voice-First Farmer Assistance System 🌾

<p align="center">
  <a href="https://github.com/ankush850/AgriSakha/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/streamlit-app-red.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/blockchain-custom%20SHA256-brightgreen" alt="Blockchain">
  <img src="https://img.shields.io/badge/ASR-Vosk%20Hindi-orange" alt="Vosk Hindi ASR">
</p>

<h3 align="center">🌟 Transforming Agriculture for India's Smallholder Farmers 🌟</h3>

<p align="center">
AgriSakha AI is a voice-first prototype that helps farmers access agricultural advice, credit scoring, and soil analysis — all in Hindi. Designed to work on basic feature phones without requiring smartphones or digital literacy.
</p>

---

## ✨ What's Built (Current Prototype)

### 🗣️ Voice AI Module (`voice_ai/`)
- **Hindi Speech Recognition** using [Vosk ASR](https://alphacephei.com/vosk/) (`vosk-model-small-hi-0.22`)
- **Hindi Text-to-Speech** using [Coqui TTS](https://github.com/coqui-ai/TTS) (`tts_models/hi/indic-tts`)
- Handles common farmer queries: pest control, loans, soil testing
- Responds in Hindi via keyword matching with actionable advice
- USSD-style menu: `1.कर्ज 2.कीट 3.मिट्टी`

### 💳 Credit Scoring Module (`credit_scoring/`)
- **`engine.py`** — Satellite-data-weighted credit scoring engine
  - Factors: Crop health (60%), Soil moisture (20%), Acreage (20%)
  - Mocks ISRO Bhuvan satellite API for field data
  - Returns score + Hindi voice response (e.g., `"क्रेडिट स्कोर: 78"`)
- **`blockchain.py`** — Custom SHA-256 blockchain for tamper-proof credit records
  - Genesis block initialization, block addition, and chain validation
  - Each credit score event is stored as an immutable on-chain record

### 🌱 Soil Analysis Module (`edge_computing/`)
- **`soil.py`** — Soil parameter analysis engine
  - Inputs: Nitrogen, Phosphorus, Potassium, pH, Organic Carbon
  - Weighted model calculates fertilizer recommendation score
  - Generates Hindi report with nutrient status (कम / सामान्य / अधिक)
  - Recommends Urea dosage in kg/acre

### 🌐 Streamlit Web App (`streamlit_app.py`)
- Interactive UI to input soil parameters and generate instant Hindi reports
- Run locally to demo the soil analysis pipeline
- Outputs Hindi fertilizer recommendations and numeric recommendation score

---

## 📁 Project Structure

```text
AgriSakha/
├── streamlit_app.py          # Streamlit web UI for soil analysis
├── config.py                 # Central config (TTS model, ASR model, thresholds)
├── voice_ai/
│   ├── core.py               # VoiceProcessor: record → transcribe → respond → speak
│   └── requirements.txt      # TTS, Vosk, sounddevice, pydub, librosa
├── credit_scoring/
│   ├── engine.py             # CreditEngine: satellite-based scoring + blockchain storage
│   └── blockchain.py         # AgriBlockchain: SHA-256 chain with validation
├── edge_computing/
│   ├── soil.py               # SoilAnalyzer: NPK/pH analysis + Hindi report generation
│   └── requirements.txt      # numpy, etc.
├── data/
│   ├── sample_queries.json   # Hindi/English test queries + USSD commands
│   ├── soil_samples.json     # Sample soil data for testing
│   ├── NFHS_5_Factsheets_Data.xls
│   └── RS_Session_246_AU1132_1.1.csv
├── docs/
│   ├── ARCHITECTURE.md
│   ├── INSTALL.md
│   └── DEMO.md
└── tests/
    ├── test_voice_ai.py
    └── test_credit_scoring.py
```

---

## 🛠️ Technology Stack

| Component         | Technology                          |
|-------------------|-------------------------------------|
| **ASR (Speech→Text)** | Vosk `vosk-model-small-hi-0.22` |
| **TTS (Text→Speech)** | Coqui TTS `tts_models/hi/indic-tts` |
| **Soil Analysis** | NumPy weighted model                |
| **Credit Scoring**| Custom satellite-weight algorithm   |
| **Blockchain**    | Custom SHA-256 chain (Python)       |
| **Web UI**        | Streamlit                           |
| **Audio**         | sounddevice, pydub, librosa         |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+

### 1. Clone the repository
```bash
git clone https://github.com/ankush850/AgriSakha.git
cd AgriSakha
```

### 2. Install Voice AI dependencies
```bash
cd voice_ai
pip install -r requirements.txt
```

### 3. Run the Streamlit Soil Analysis App
```bash
cd ..
pip install streamlit numpy
streamlit run streamlit_app.py
```

### 4. Run Credit Scoring Engine
```bash
python credit_scoring/engine.py
```

### 5. Run Voice Processor (requires microphone)
```bash
python voice_ai/core.py
```

### 6. Run Tests
```bash
python -m pytest tests/
```

For detailed setup, see [`docs/INSTALL.md`](docs/INSTALL.md).

---

## 🎯 Sample Queries (from `data/sample_queries.json`)

| Hindi Query | English | Response |
|---|---|---|
| `मेरी फसल में कीड़े लग गए हैं` | My crop has pests | नीम तेल 5 मिली/लीटर, 3 दिन अंतराल |
| `गेहूं के लिए कितना यूरिया डालें?` | How much urea for wheat? | 50 किलो/एकड़ |
| `मेरा क्रेडिट स्कोर क्या है?` | What is my credit score? | Score + loan eligibility |
| `आज टमाटर की कीमत?` | Today's tomato price? | ₹40/किलो (मंडी भोपाल) |

### USSD Commands
| Code | Action |
|------|--------|
| `*123*1#` | Pest control menu |
| `*123*2#` | Loan eligibility check |

---

## ⚙️ Configuration (`config.py`)

```python
class Config:
    TTS_MODEL = "tts_models/hi/indic-tts"
    ASR_MODEL = "models/vosk-model-small-hi-0.22"
    NODE_ADDRESS = "127.0.0.1:5000"      # Blockchain node
    SOIL_THRESHOLDS = {
        'nitrogen':   (30, 50),           # mg/kg
        'phosphorus': (15, 40),
        'potassium':  (20, 50)
    }
```

---

## 📊 Data Sources

| Dataset | Source | Use Case |
|---------|--------|----------|
| NFHS-5 Factsheets | data.gov.in | Agricultural demographic context |
| Rajya Sabha AU data | sansad.in | Policy reference |
| Sample Queries | Field recordings (mock) | NLP testing |
| Soil Samples | Synthetic | Soil analyzer testing |

---

## 🙏 Acknowledgments

* **AI4Bharat** for Hindi NLP tools and IndicTTS support.
* **Alphacephei (Vosk)** for lightweight offline Hindi ASR.
* **ISRO Bhuvan** for satellite data API inspiration.
* **The/Nudge Institute** for the Pragati AI for Impact Hackathon platform.
