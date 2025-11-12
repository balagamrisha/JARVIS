# IRIS - Intelligent Responsive Interactive System

**A multi-mode AI voice assistant designed for developers, students, and productivity enthusiasts**

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-orange.svg)
![Modes](https://img.shields.io/badge/modes-3-brightgreen.svg)

---
## ABOUT
## 🎯 What is IRIS?

IRIS is not just another voice assistant - it's a **specialized AI companion** with three distinct modes, each optimized for specific tasks:

1. **👨‍💻 Developer Mode** - Your AI pair programmer
2. **📅 Personal Mode** - Your daily life manager  
3. **📚 Learning Mode** - Your study companion

Instead of doing random tasks poorly, IRIS excels at what it's designed for: Switch modes based on what you're doing, and get context-aware, intelligent assistance.

---

## ✨ Why IRIS is Different?

| Feature | Generic Voice Assistants | IRIS |
|---------|-------------------------|------|
| Purpose | One-size-fits-all | Specialized modes |
| Code Generation | Basic snippets | Full functions with tests |
| Context | Forgets quickly | Persistent project memory |
| Learning | Generic answers | Study-optimized responses |
| Cost | Subscription required | 100% free APIs |
| Customization | Limited | Fully open source |

---

## 🎭 The Three Modes

### 🔧 **Mode 1: Developer Assistant**

Your AI pair programmer. Code faster, debug smarter.

**What it does:**
- 💻 **Voice-controlled code generation** - "Create a function to sort users by age"
- 📝 **Code explanation** - "Explain this code" (reads from clipboard)
- ⚡ **Code improvement** - "Optimize this function" 
- 🔍 **Smart search** - "Search Stack Overflow for async errors"
- 📚 **Documentation lookup** - "Python docs for decorators"
- 🛠️ **Tool integration** - "Open VS Code with my project"

**Perfect for:**
- Writing functions and classes by voice
- Understanding unfamiliar code
- Quick Stack Overflow/documentation access
- Hands-free coding while thinking out loud

---

### 📅 **Mode 2: Personal Assistant**

Your daily life manager. Never miss a thing.

**What it does:**
- ⏰ **Reminders & timers** - "Remind me to call mom at 6 PM"
- 🌤️ **Weather & news** - "What's the weather in Hyderabad?"
- 🗓️ **Schedule management** - "What's on my schedule today?"
- 🧮 **Quick calculations** - "Calculate 15% tip on 850 rupees"
- 📍 **Time zones** - "What time is it in Tokyo?"
- 🧠 **Personal memory** - Learns your preferences and habits

**Perfect for:**
- Managing your daily schedule
- Staying informed about weather/news
- Setting reminders hands-free
- Quick information lookup

---

### 📚 **Mode 3: Learning Assistant**

Your study companion. Learn faster, retain longer.

**What it does:**
- 🎓 **Concept explanations** - "Explain quantum computing"
- ⏱️ **Study timer (Pomodoro)** - "Start a 25-minute study session"
- 📝 **Voice notes** - "Take a note: Machine learning uses neural networks"
- 🗣️ **Topic summaries** - "Summarize the French Revolution"
- 📊 **Quiz generation** *(planned)* - Test your knowledge
- 📄 **Document summarization** *(planned)* - Summarize PDFs/articles

**Perfect for:**
- Studying complex topics
- Taking quick voice notes
- Structured study sessions
- Understanding difficult concepts

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 (versions 3.8-3.11 supported)
- Microphone
- Internet connection
- Clipboard access (for code features)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/balagamrisha/IRIS.git
cd IRIS
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Get FREE API Keys**

| Service | Free Tier | Purpose | Sign Up |
|---------|-----------|---------|---------|
| **Deepgram** | $200 credit | Speech-to-text | [console.deepgram.com](https://console.deepgram.com/) |
| **Groq** | Unlimited | AI brain (Llama 3.3) | [console.groq.com](https://console.groq.com/) |
| **ElevenLabs** | 10k chars/month | Text-to-speech | [elevenlabs.io](https://elevenlabs.io/) |

4. **Configure environment**

Create a `.env` file in the project root:
```env
DEEPGRAM_API_KEY=your_deepgram_key_here
GROQ_API_KEY=your_groq_key_here
ELEVENLABS_API_KEY=your_elevenlabs_key_here
```

5. **Run IRIS**
```bash
# Terminal 1: Web interface (optional)
python display.py

# Terminal 2: Voice assistant
python main.py
```

---

## 💬 Usage Examples

### 👨‍💻 Developer Mode Commands

**Code Generation:**
```
"Create a Python function to validate email addresses"
"Write a REST API endpoint for user login"
"Generate a React component for a button"
```

**Code Analysis:**
```
*Copy code to clipboard*
"Explain this code"
"What does this function do?"
"Improve this code"
"Add error handling to this"
```

**Development Workflow:**
```
"Open VS Code"
"Search Stack Overflow for Python asyncio"
"Python documentation for file handling"
"Open my GitHub"
```

### 📅 Personal Mode Commands
```
"What time is it?"
"What's the weather in Hyderabad?"
"Remind me to submit assignment at 5 PM"
"Set a timer for 25 minutes"
"What's on my schedule today?"
```

### 📚 Learning Mode Commands
```
"Explain machine learning like I'm 5"
"Start a study session" (Pomodoro timer)
"Take a note: Neural networks have multiple layers"
"Tell me about the Renaissance"
```

### 🎛️ Mode Switching
```
"Switch to developer mode"
"Switch to personal mode"
"Switch to study mode"
"What mode am I in?"
```

---

## 🏗️ Project Structure
```
IRIS/
├── main.py                 # Core assistant logic
├── display.py              # Web interface (Taipy)
├── record.py               # Audio recording module
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed)
│
├── generated_code/         # AI-generated code files
├── audio/                  # Audio recordings
├── user_data.json          # Personal memory
├── mode_config.json        # Current mode settings
│
├── README.md               # This file
└── DEVELOPMENT_LOG.md      # Technical notes
```

---

## 🎨 Customization

### Change Assistant Personality
Edit `main.py` line 30:
```python
context = "You are IRIS, a [your description]..."
```

### Add Custom Commands
In the appropriate mode handler function:
```python
def handle_developer_commands(text: str):
    if "your custom command" in text.lower():
        # Your code here
        return True, "Your response"
```

### Change Voice
Modify ElevenLabs voice ID (line ~120):
```python
voice_id="pNInz6obpgDQGcFmaJgB"  # Try different voice IDs
```

### Add New Mode
Create a new mode handler function and integrate into the mode system!

---

## 📊 Current Status

**Version:** 2.0-dev  
**Active Development:** Yes 🚧

### ✅ Completed Features

**Core System:**
- ✅ Multi-API integration (Deepgram, Groq, ElevenLabs)
- ✅ Continuous voice interaction loop
- ✅ Error handling and logging
- ✅ User memory system (remembers name/preferences)
- ✅ Smart command routing

**Developer Mode:**
- ✅ Voice-controlled code generation
- ✅ Clipboard integration (explain/improve code)
- ✅ Stack Overflow search integration
- ✅ Python documentation quick access
- ✅ File creation with smart naming
- ✅ Multi-language support (Python, JS, Java, C++)

**Personal Mode:**
- ✅ Time/date queries
- ✅ Application control (Chrome, VS Code, Spotify)
- ✅ Web search integration
- ✅ YouTube playback
- ✅ Random utilities (coin flip, dice roll)

**Learning Mode:**
- ⏳ In development

### 🔄 In Progress

**Developer Mode:**
- 🔨 Git voice commands
- 🔨 Project context memory
- 🔨 Code template library

**Personal Mode:**
- 🔨 Weather API integration
- 🔨 Reminder system
- 🔨 News briefing

**Learning Mode:**
- 🔨 Wikipedia integration
- 🔨 Pomodoro timer
- 🔨 Voice note taking

### 📋 Planned Features

- [ ] Mode switching system
- [ ] Enhanced web dashboard
- [ ] Emotion detection
- [ ] Real-time conversation (interrupt capability)
- [ ] Multi-language support
- [ ] Quiz generation (Learning Mode)
- [ ] Calendar integration (Personal Mode)
- [ ] Code review assistant (Developer Mode)

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.11** - Primary language
- **Deepgram API** - Speech recognition ($200 free credit)
- **Groq API** - LLM inference with Llama 3.3 70B (free)
- **ElevenLabs API** - Neural voice synthesis (10k chars/month)
- **Pygame** - Audio playback
- **Taipy** - Web interface
- **Pyperclip** - Clipboard integration

### Why These Technologies?

| Technology | Why We Chose It |
|-----------|-----------------|
| **Groq over OpenAI** | Free, faster inference, comparable quality |
| **Deepgram** | Most accurate STT, generous free tier |
| **ElevenLabs** | Most natural-sounding voices |
| **Python 3.11** | Best library support, async capabilities |

---

## 🎯 Use Cases

### For Developers
- Code while walking/exercising
- Quickly generate boilerplate code
- Understand unfamiliar codebases
- Access documentation hands-free
- Debug with voice explanations

### For Students
- Take voice notes during lectures
- Study with Pomodoro technique
- Get concept explanations
- Quiz yourself on topics
- Manage study schedules

### For Everyone
- Manage daily tasks
- Set reminders
- Get weather updates
- Quick calculations
- Hands-free productivity

---

## 🤝 Contributing

This is a personal learning project as I'm experimenting with tools and ideas, but contributions are welcome!

**Areas for contribution:**
- New mode handlers 
- Additional voice commands
- UI improvements
- Documentation
- Bug fixes

---

## 📝 Development Philosophy

**Why did I want to structure IRIS this way?**

1. **Specialized > Generic** - Three focused modes are integrated
2. **Free > Paid** - Students shouldn't pay for learning tools
3. **Practical > Flashy** - Features that solve real problems
4. **Open > Closed** - Fully customizable and transparent
5. **Learning-First** - Built to teach AI integration concepts

---

## 📖 Documentation

- **[DEVELOPMENT_LOG.md](DEVELOPMENT_LOG.md)** - Technical decisions, issues solved, learning notes
- **[API_REFERENCE.md](API_REFERENCE.md)** - Function documentation *(coming soon)*
- **[MODE_GUIDE.md](MODE_GUIDE.md)** - Detailed guide for each mode *(coming soon)*

---

## 🙏 Acknowledgments

**Built upon:**
- [JARVIS](https://github.com/AlexandreSajus/JARVIS) by Alexandre Sajus - Original foundation
- [Groq](https://groq.com/) - Lightning-fast LLM inference
- [Deepgram](https://deepgram.com/) - Industry-leading STT
- [ElevenLabs](https://elevenlabs.io/) - Realistic voice synthesis

**Inspired by:**
- A thought to make useful AI assistant which isn't generic 
- Making AI accessible to students

---

## 📄 License
The same one as the forked project.

---

## 📬 Contact

**Developer:** Balagam Risha Raj
**Project Link:**(https://github.com/balagamrisha/IRIS)

---

## 🚦 Project Roadmap

### Phase 1: Foundation ✅ (Completed)
- Core voice pipeline
- Basic command system
- User memory

### Phase 2: Developer Mode 🔄 (Current)
- Code generation
- Clipboard integration
- Tool integration

### Phase 3: Personal Mode ⏳ (Next)
- Weather API
- Reminders
- Calendar

### Phase 4: Learning Mode ⏳
- Study timer
- Note taking
- Wikipedia

### Phase 5: Polish ⏳
- Mode switching
- Enhanced UI
- Performance optimization
