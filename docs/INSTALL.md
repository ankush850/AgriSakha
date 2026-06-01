## AgriSakha Installation Guide

### System Requirements
- Ubuntu 20.04 LTS
- Python 3.8
- 2GB RAM minimum

### 1. Base Installation
```bash
sudo apt update
sudo apt install -y python3.8 python3.8-venv ffmpeg portaudio19-dev
```

### 2. Virtual Environment
```bash
python3.8 -m venv agrisakha
source agrisakha/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt

# Install Hindi ASR model
wget https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip
unzip vosk-model-small-hi-0.22.zip -d models/
```

### 4. Verify Installation
```bash
python3 -m voice_ai.core --test
python3 -m credit_scoring.engine --demo
```