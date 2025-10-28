# IRIS - Voice Assistant

A voice-controlled AI assistant with speech recognition, natural language processing, and task automation capabilities.

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-orange.svg)

## 📌 About

IRIS is a customized voice assistant built by forking and extensively enhancing the [JARVIS project](https://github.com/AlexandreSajus/JARVIS). Key improvements include migration to free APIs, task automation, and intelligent command routing.

### What Makes IRIS Different?

| Feature | Original JARVIS | IRIS |
|---------|----------------|------|
| LLM API | OpenAI (paid) | Groq (free) |
| Command Processing | All via API | Smart local routing |
| Personality | Witty | Humble & approachable |
| Task Automation | Limited | 10+ commands |
| Cost | ~$0.002/request | $0 |

## ✨ Features

### 🎤 Voice Interaction
- Real-time speech-to-text transcription (Deepgram)
- Natural language understanding (Groq/Llama 3.3 70B)
- High-quality voice synthesis (ElevenLabs)
- Continuous conversation loop

### 🤖 Smart Command Routing
Processes simple commands locally for instant responses:
- ⏰ Time and date queries
- 💻 Application control (Chrome, VSCode, Spotify)
- 🔍 Web search integration
- 🎵 YouTube playback
- 🎲 Random utilities (coin flip, dice roll)

### 🧠 AI-Powered Responses
For complex queries, IRIS uses Groq's Llama 3.3 70B model to provide:
- Intelligent, context-aware answers
- Customizable personality
- Concise, friendly responses

## 🛠️ Tech Stack

- **Python 3.11** - Core language
- **Deepgram API** - Speech-to-text (free $200 credit)
- **Groq API** - LLM inference (free tier)
- **ElevenLabs API** - Text-to-speech (10k chars/month free)
- **Pygame** - Audio playback
- **Taipy** - Web interface

## 🚀 Installation

### Prerequisites
- Python 3.11 (versions 3.8-3.11 supported)
- Microphone
- Internet connection

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/IRIS.git
cd IRIS
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Get API Keys** (all free tiers)

| Service | Free Tier | Sign Up Link |
|---------|-----------|--------------|
| Deepgram | $200 credit | [console.deepgram.com](https://console.deepgram.com/) |
| Groq | Unlimited | [console.groq.com](https://console.groq.com/) |
| ElevenLabs | 10k chars/month | [elevenlabs.io](https://elevenlabs.io/) |

4. **Configure environment**

Create a `.env` file in the project root:
```env
DEEPGRAM_API_KEY=your_deepgram_key
GROQ_API_KEY=your_groq_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

5. **Run IRIS**
```bash
# Terminal 1: Web interface
python display.py

# Terminal 2: Voice assistant
python main.py
```

## 💬 Usage Examples

Once running, try these commands:

**System Queries:**
- "What time is it?"
- "What's today's date?"

**Task Automation:**
- "Open Chrome"
- "Open VS Code"
- "Search Google for machine learning tutorials"
- "Play Bohemian Rhapsody on YouTube"

**AI Conversations:**
- "Explain quantum computing"
- "What's the weather like?" (uses AI, not weather API yet)
- "Tell me a fun fact"

**Utilities:**
- "Flip a coin"
- "Roll a dice"

Press `Ctrl+C` in either terminal to stop.

## 🎨 Customization

### Change Assistant Personality
Edit `main.py` line 30:
```python
context = "You are Iris, a [your custom personality here]..."
```

### Add Custom Commands
In `main.py`, locate the `handle_local_commands()` function and add:
```python
if "your command" in text_lower:
    # Your code here
    return True, "Your response"
```

### Change Voice
Modify `voice_id` in the ElevenLabs section (line 120):
```python
voice_id="pNInz6obpgDQGcFmaJgB"  # Change to different voice ID
```

## 📊 Project Status

**Current Version:** 1.0-dev  
**Status:** 🚧 Active Development

### ✅ Completed
- Core voice interaction pipeline
- Multi-API integration (Deepgram, Groq, ElevenLabs)
- Local command routing system
- Task automation (10+ commands)
- Error handling and logging
- Custom personality implementation

### 🔄 In Progress
- User memory system (remember preferences)
- Enhanced web dashboard

### 📋 Planned
- Voice-controlled code generation
- Emotion detection and adaptive responses
- Real-time conversation (interrupt capability)
- Multi-language support
- Weather API integration
- Reminder/timer system

## 📁 Project Structure
```
IRIS/
├── main.py              # Core assistant logic
├── display.py           # Web interface
├── record.py            # Audio recording module
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed)
├── audio/              # Audio files directory
├── README.md           # This file
└── DEVELOPMENT_LOG.md  # Technical development notes
```

## 🤝 Contributing

This is a personal learning project, but suggestions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Fork and create your own version
- Share improvements

## 📝 Development Log

See [DEVELOPMENT_LOG.md](DEVELOPMENT_LOG.md) for:
- Technical decisions and rationale
- Issues encountered and solutions
- Learning outcomes
- API migration notes

## Acknowledgments

This project builds upon [JARVIS](https://github.com/AlexandreSajus/JARVIS) by Alexandre Sajus. The original project provided an excellent foundation for learning voice assistant development.

## 📄 License

[Specify license - typically same as original project]

## 📬 Contact

[Your Name]  
GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

**Note:** This project uses free API tiers. Ensure you stay within rate limits for continued free access.