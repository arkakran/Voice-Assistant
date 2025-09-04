from src.audio.speech_to_text import SpeechToText
from src.audio.text_to_speech import TextToSpeech
from src.hardware.hardware_controller import HardwareController
from src.utils.logger import Logger
from src.ai.language_model import SimpleLanguageModel


def main():
    print("=== LOCAL VOICE ASSISTANT ===")
    logger = Logger()
    stt = SpeechToText(logger=logger)
    tts = TextToSpeech(logger=logger)
    hardware = HardwareController(logger=logger)
    slm = SimpleLanguageModel(
        model_name="distilgpt2",
        logger=logger,
        cache_dir="C:\\Users\\Aryan Kakran\\.cache\\huggingface\\hub"
    )

    while True:
        try:
            print("\nListening...")
            command = stt.listen()

            if not command.strip(): 
                print("⚠️ Empty transcription, skipping...")
                continue

            print(f"You: {command}")

            # Build LM prompt
            prompt = f"User command: {command}. Generate response and action:"
            response = slm.generate_response(prompt)

            # Default response (LM generated)
            final_response = f" Assistant: {response}"

            # Simple intent matching for hardware
            lower_cmd = command.lower()
            if "turn on light" in lower_cmd:
                hardware.execute_action("light", "turn on")
                final_response = "Turning on the light. Light turned on successfully."
            elif "turn off light" in lower_cmd:
                hardware.execute_action("light", "turn off")
                final_response = "Turning off the light. Light turned off successfully."
            # 🔌 Add more devices/actions here later

            print(final_response)
            tts.speak(final_response)

        except KeyboardInterrupt:
            print("\n\n Shutting down......")
            break


if __name__ == "__main__":
    main()
