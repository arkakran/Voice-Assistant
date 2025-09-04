import whisper
import numpy as np
import soundfile as sf
import sounddevice as sd

class SpeechToText:
    def __init__(self, model_name="small", logger=None):
        self.logger = logger
        # Force FP32 by setting device="cpu"
        self.model = whisper.load_model(model_name, device="cpu")

    def listen(self, duration=5, fs=8000):
        """
        Record audio from microphone and transcribe using Whisper
        """
        print(" Recording...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        audio = np.squeeze(audio)

        sf.write("temp.wav", audio, fs)
        
        # Force FP32
        result = self.model.transcribe("temp.wav", fp16=False)
        text = result.get("text", "").strip()

        if self.logger:
            self.logger.log_speech(text)

        return text

