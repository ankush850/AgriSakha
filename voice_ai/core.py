import os
import sounddevice as sd
import numpy as np
from TTS.api import TTS
import logging
from vosk import Model, KaldiRecognizer
import wave

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VoiceProcessor:
    def __init__(self):
        # Initialize Hindi TTS
        self.tts = TTS(model_name="tts_models/hi/indic-tts")
        
        # Load Vosk Hindi ASR model (lightweight alternative)
        self.asr_model = Model(lang="hi-in")
        
        # Audio config
        self.sample_rate = 16000
        self.audio_duration = 5  # seconds

    def record_audio(self):
        """Record audio from microphone with error handling"""
        try:
            logger.info("Recording... Speak now (Hindi)")
            audio = sd.rec(
                int(self.audio_duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype='float32'
            )
            sd.wait()
            return audio
        except Exception as e:
            logger.error(f"Recording failed: {str(e)}")
            raise

    def transcribe(self, audio_path):
        """Convert speech to text with fallback"""
        try:
            wf = wave.open(audio_path, "rb")
            rec = KaldiRecognizer(self.asr_model, wf.getframerate())
            
            result = ""
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    result += rec.Result()
            
            return result if result else "कृपया पुनः प्रयास करें"
        except Exception as e:
            logger.error(f"Transcription failed: {str(e)}")
            return "सिस्टम त्रुटि"

    def process_query(self, text):
        """Generate agricultural response"""
        responses = {
            "कीट": "नीम तेल 5 मिली प्रति लीटर पानी में मिलाएं। 82% प्रभावी।",
            "कर्ज": "आप ₹75,000 के पात्र हैं। स्वीकार करने के लिए 1 भेजें",
            "मिट्टी": "मिट्टी जाँच के लिए कृपया नमूना दें"
        }
        return responses.get(text, "USSD मेनू: 1.कर्ज 2.कीट 3.मिट्टी")

    def run(self):
        """Main execution flow"""
        try:
            # 1. Record audio
            audio = self.record_audio()
            audio_file = "query.wav"
            sd.write(audio_file, audio, self.sample_rate)
            
            # 2. Transcribe
            text = self.transcribe(audio_file)
            logger.info(f"Recognized: {text}")
            
            # 3. Generate response
            response = self.process_query(text)
            
            # 4. Speak response
            self.tts.tts_to_file(text=response, file_path="response.wav")
            os.system("aplay response.wav")
            
        finally:
            # Cleanup
            for f in [audio_file, "response.wav"]:
                if os.path.exists(f):
                    os.remove(f)

if __name__ == "__main__":
    VoiceProcessor().run()