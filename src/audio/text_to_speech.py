import pyttsx3

class TextToSpeech:
    def __init__(self, logger=None, rate=150, volume=1.0, voice=None):
        self.logger = logger
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        if voice:
            self.engine.setProperty('voice', voice)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        if self.logger:
            self.logger.log_speech(text)
