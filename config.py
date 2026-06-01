import os

class Config:
    # Voice AI
    TTS_MODEL = "tts_models/hi/indic-tts"
    ASR_MODEL = "models/vosk-model-small-hi-0.22"
    
    # Blockchain
    NODE_ADDRESS = os.getenv("NODE_ADDR", "127.0.0.1:5000")
    
    # Edge Computing
    SOIL_THRESHOLDS = {
        'nitrogen': (30, 50),
        'phosphorus': (15, 40),
        'potassium': (20, 50) 
    }