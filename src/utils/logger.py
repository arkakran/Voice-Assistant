import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir="logs"):
        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir
        self.hardware_log_file = os.path.join(log_dir, "hardware.log")
        self.speech_log_file = os.path.join(log_dir, "speech.log")
        self.error_log_file = os.path.join(log_dir, "error.log")

    def log_hardware_event(self, message):
        self._write_log(self.hardware_log_file, message)

    def log_speech(self, message):
        self._write_log(self.speech_log_file, message)

    def log_error(self, context, message):
        self._write_log(self.error_log_file, f"[{context}] {message}")

    def _write_log(self, filepath, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filepath, "a", encoding="utf-8") as f:  
            f.write(f"{timestamp} - {message}\n")
