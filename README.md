project:
  name: "Local AI Voice Assistant"
  description: "A fully offline AI voice assistant capable of interpreting user commands, generating responses using a small language model, converting responses to speech, and simulating hardware actions like turning on/off lights or fans."
  features:
    - "Offline Speech Recognition (ASR) with Whisper"
    - "Simple Language Model (SLM) using DistilGPT2"
    - "Text-to-Speech (TTS) using pyttsx3"
    - "Hardware Simulation for lights/fans"
    - "Interactive multiple command loop"
    - "Logging for speech, hardware actions, and errors"

system_architecture:
  flow:
    - "User Voice → Microphone → ASR (Whisper) → Simple Language Model (DistilGPT2)"
    - "Audio Recording"
    - "Text Command Parsing"
    - "TTS (pyttsx3) ← Response Text ← Decision / Action"
    - "Speaker Output"
    - "Optional: Hardware Controller (Simulated GPIO / Fan / Light)"
  explanation:
    User_Voice: "User speaks commands like 'Turn on the light.'"
    ASR_Whisper: "Converts recorded speech to text."
    SLM_DistilGPT2: "Processes text command, generates response text, and decides the hardware action."
    TTS_pyttsx3: "Converts response text to audio for playback."
    Speaker_Output: "Plays the response audio."
    Hardware_Controller: "Executes the action (light/fan) on GPIO pins; simulated in current implementation."

project_structure:
  root: "voice_assistant/"
  files:
    - "assistant.py: Main script to run the assistant"
    - "requirements.txt: Python dependencies"
    - "src/audio/speech_to_text.py: ASR (Whisper)"
    - "src/audio/text_to_speech.py: TTS (pyttsx3)"
    - "src/hardware/hardware_controller.py: Simulated GPIO actions"
    - "src/ai/language_model.py: DistilGPT2-based SLM"
    - "src/utils/logger.py: Logging for speech, hardware, errors"
    - "README.md: Project documentation"

requirements:
  python_version: ">=3.9"
  packages:
    - "torch>=2.1.0"
    - "transformers>=4.30.0"
    - "pyttsx3>=2.90"
    - "sounddevice>=0.4.6"
    - "numpy>=1.24.0"
    - "simpleaudio>=1.0.4"
    - "soundfile>=0.12.1"
    - "whisper @ git+https://github.com/openai/whisper.git"

installation:
  steps:
    - "git clone <your_repo_url>"
    - "cd voice_assistant"
    - "python -m venv venv"
    - "venv\\Scripts\\activate  # Windows"
    - "pip install -r requirements.txt"
    - "Pre-download models for offline usage in HuggingFace cache"

usage:
  run_command: "python assistant.py"
  interaction_steps:
    - "Speak commands like 'Turn on light', 'Turn off fan', 'Wave hello'"
    - "Assistant records voice and converts to text (ASR)"
    - "SLM interprets text and generates response"
    - "Response converted to audio (TTS)"
    - "Optional simulated hardware action executed and logged"
    - "Press Ctrl+C to exit"

example_interaction:
  - "🎤 Listening..."
  - "🎙️ Recording..."
  - "👤 You: Please turn on light."
  - "🤖 Assistant: Turning on the light."
  - "⚡ [SIMULATION] TURN ON light (Pin: PIN_17)"

hardware_simulation:
  actions: "Light/Fan/Servo Simulation printed and logged"
  optional_extension:
    - "Raspberry Pi GPIO"
    - "Arduino via pySerial"
    - "Jetson board"
  class: "HardwareController"

logging:
  location: "logs/"
  types:
    - "speech.log: all transcribed text"
    - "hardware.log: all simulated hardware actions"
    - "error.log: any errors during execution"

notes:
  - "Keep models cached for offline use (~C:\\Users\\Aryan Kakran\\.cache\\huggingface\\hub)"
  - "Use small/lightweight models to minimize CPU/RAM usage"
  - "TTS quality can be improved using Coqui or Silero"
  - "Prompt design for SLM should avoid repetitive outputs"
  - "Entire pipeline works offline; no cloud API dependency"

future_extensions:
  - "Replace simulated hardware with real GPIO actions"
  - "Integrate with smart home devices"
  - "Improve TTS quality and voice variety"
  - "Add more complex command understanding and multi-step actions"

