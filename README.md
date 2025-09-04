# Local AI Voice Assistant

A fully offline AI voice assistant capable of interpreting user commands, generating responses using a small language model, converting responses to speech, and simulating hardware actions like turning on/off lights or fans.

## 🌟 Features

- **Offline Speech Recognition (ASR)**: Uses Whisper (small) to transcribe voice commands locally
- **Simple Language Model (SLM)**: Uses DistilGPT2 to interpret commands and generate responses
- **Text-to-Speech (TTS)**: Converts response text to audio using pyttsx3
- **Hardware Simulation**: Simulates GPIO actions for lights, fans, or other devices
- **Interactive Loop**: Supports multiple consecutive commands in one session
- **Logging**: Tracks speech, hardware actions, and errors

## 🏗️ System Architecture

```
User Voice → Microphone → ASR (Whisper) → Simple Language Model (DistilGPT2)
    ↓                         ↓                           ↓
Audio Recording      Text Command Parsing        Decision / Action
    ↓                         ↓                           ↓
TTS (pyttsx3) ← Response Text ←─────────────────────────────┘
    ↓
Speaker Output
    ↓
Optional: Hardware Controller (Simulated GPIO / Fan / Light)
```

## 📁 Project Structure

```
voice_assistant/
├── assistant.py                    # Main script to run the assistant
├── requirements.txt                # Python dependencies
├── src/
│   ├── audio/
│   │   ├── speech_to_text.py      # ASR (Whisper)
│   │   └── text_to_speech.py      # TTS (pyttsx3)
│   ├── hardware/
│   │   └── hardware_controller.py # Simulated GPIO actions
│   ├── ai/
│   │   └── language_model.py      # DistilGPT2-based SLM
│   └── utils/
│       └── logger.py              # Logging for speech, hardware, errors
└── README.md
```

## 📋 Requirements

- **Python**: 3.9+
- **Dependencies**: Listed in `requirements.txt`

```txt
torch>=2.1.0
transformers>=4.30.0
pyttsx3>=2.90
sounddevice>=0.4.6
numpy>=1.24.0
simpleaudio>=1.0.4
soundfile>=0.12.1
whisper @ git+https://github.com/openai/whisper.git
```

> **Note:** All models (Whisper & DistilGPT2) should be pre-downloaded in your HuggingFace cache directory (`C:\Users\[Username]\.cache\huggingface\hub`) for offline use.

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <your_repo_url>
cd voice_assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Pre-download Models for Offline Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# DistilGPT2
model = AutoModelForCausalLM.from_pretrained("distilgpt2", cache_dir=r"C:\Users\[Username]\.cache\huggingface\hub")
tokenizer = AutoTokenizer.from_pretrained("distilgpt2", cache_dir=r"C:\Users\[Username]\.cache\huggingface\hub")

# Whisper (small) - will be downloaded automatically when first used
```

## 🎯 Usage

### Run the Assistant
```bash
python assistant.py
```

### Voice Commands
The assistant responds to commands such as:
- "Turn on light"
- "Turn off fan"
- "Wave hello"

### Process Flow
1. **Voice Input**: Speak your command
2. **ASR Processing**: Whisper converts speech to text
3. **Language Processing**: DistilGPT2 interprets the command
4. **Response Generation**: Creates appropriate response
5. **TTS Output**: Converts response to speech
6. **Hardware Action**: Simulates device control (optional)
7. **Logging**: Records all actions

### Exit
Press `Ctrl+C` to stop the assistant

## 💬 Example Interaction

```
🎤 Listening...
🎙️ Recording...
👤 You: Please turn on light.
🤖 Assistant: Turning on the light.
⚡ [SIMULATION] TURN ON light (Pin: PIN_17)
```

## 🔧 Hardware Simulation

### Current Implementation
- **Light/Fan/Servo Simulation**: Actions are printed to console and logged
- **Pin Mapping**: Simulated GPIO pin assignments
- **Action Logging**: All hardware commands are recorded

### Future GPIO Integration
The system is designed to easily integrate with real hardware:
- **Raspberry Pi GPIO**
- **Arduino via pySerial**
- **NVIDIA Jetson boards**

Use the `HardwareController` class to map commands to actual pins and actions.

## 📊 Logging

Logs are automatically stored in the `logs/` directory:

- **`speech.log`** – All transcribed text and voice interactions
- **`hardware.log`** – All simulated/actual hardware actions
- **`error.log`** – System errors and exceptions

## 📝 Notes & Recommendations

### Performance Optimization
- Keep models cached locally for true offline operation
- Use lightweight models to minimize CPU/RAM usage
- Optimize prompt design for SLM to prevent repetitive outputs

### Quality Improvements
- **TTS Enhancement**: Consider upgrading to Coqui TTS or Silero for better voice quality
- **ASR Accuracy**: Fine-tune Whisper model for specific use cases
- **Response Quality**: Improve prompt engineering for more natural responses

### System Requirements
- **RAM**: Minimum 4GB recommended (8GB+ for better performance)
- **Storage**: ~2GB for cached models
- **Microphone**: Any USB or built-in microphone
- **Speakers**: Audio output device required

## 🔮 Future Extensions

### Hardware Integration
- [ ] Replace simulated hardware with real GPIO actions
- [ ] Integrate with smart home devices (Philips Hue, etc.)
- [ ] Support for multiple device types and protocols

### Feature Enhancements
- [ ] Improve TTS quality and voice variety
- [ ] Add wake word detection
- [ ] Implement multi-step command sequences
- [ ] Add voice training for better recognition
- [ ] Support for multiple languages

### Advanced Capabilities
- [ ] Context-aware conversations
- [ ] Learning user preferences
- [ ] Integration with calendar and reminders
- [ ] Weather and news updates (with internet connection)
