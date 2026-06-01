import unittest
from unittest.mock import patch
from voice_ai.core import VoiceProcessor

class TestVoiceAI(unittest.TestCase):
    @patch('sounddevice.rec')
    def test_recording(self, mock_rec):
        mock_rec.return_value = np.zeros(80000)
        vp = VoiceProcessor()
        audio = vp.record_audio()
        self.assertEqual(len(audio), 80000)

    def test_pest_response(self):
        vp = VoiceProcessor()
        response = vp.process_query("कीट")
        self.assertIn("नीम तेल", response)

if __name__ == '__main__':
    unittest.main()