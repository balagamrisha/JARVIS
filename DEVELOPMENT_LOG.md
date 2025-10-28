\# 📚 DEVELOPMENT LOG - IRIS Voice Assistant



\## Project Overview

IRIS is a voice-controlled AI assistant built by forking and extensively customizing the open-source JARVIS project. The assistant integrates multiple APIs to provide speech-to-text, natural language processing, text-to-speech, and system automation capabilities.



\*\*Original Repository:\*\* \[JARVIS by AlexandreSajus](https://github.com/AlexandreSajus/JARVIS)  

\*\*Tech Stack:\*\* Python 3.11, Deepgram API, Groq (Llama 3.3), ElevenLabs API, Pygame, Taipy  

\*\*Development Period:\*\* October 25-27, 2025



---



\## 🎓 Technical Skills Developed



\### 1. Multi-API Integration

Successfully integrated three distinct APIs with different authentication mechanisms:

\- \*\*Deepgram:\*\* Real-time speech-to-text transcription

\- \*\*Groq:\*\* Large language model inference (Llama 3.3 70B)

\- \*\*ElevenLabs:\*\* Neural text-to-speech synthesis



Implemented secure credential management using environment variables and the `python-dotenv` library.



\### 2. Dependency Resolution \& Package Management

\- Resolved complex dependency conflicts in a legacy codebase

\- Managed version-specific package requirements (`deepgram-sdk==0.3.0`)

\- Worked around native compilation requirements using pre-built wheels

\- Handled cross-platform compatibility issues (Windows-specific solutions)



\### 3. Legacy Code Modernization

Adapted a 2-year-old codebase to current API standards:

\- Migrated from deprecated API methods to modern implementations

\- Updated authentication patterns across multiple services

\- Refactored synchronous code patterns while maintaining async operations

\- Implemented proper error handling for external service calls



\### 4. System Integration \& Automation

Developed local command routing system using Python's standard library:

\- Process control with `subprocess` module

\- Cross-platform compatibility via `platform` detection

\- Browser automation using `webbrowser` module

\- Natural language intent parsing for command extraction



\### 5. AI Prompt Engineering

Designed system prompts to control AI behavior:

\- Personality customization through context engineering

\- Response format constraints

\- Tone and verbosity control



---



\## 🐛 Critical Issues Resolved



\### Issue #1: Python Version Incompatibility

\*\*Error:\*\* `ModuleNotFoundError: No module named 'distutils.msvccompiler'`  

\*\*Cause:\*\* Python 3.14 removed the `distutils` module required by Pygame  

\*\*Resolution:\*\* Downgraded to Python 3.11.9 (project requirement: Python 3.8-3.11)  

\*\*Impact:\*\* Highlighted importance of checking compatibility matrices before setup



---



\### Issue #2: Native Dependency Compilation Failure

\*\*Error:\*\* `error: Microsoft Visual C++ 14.0 or greater is required`  

\*\*Cause:\*\* `webrtcvad` package requires C++ compilation, build tools not installed  

\*\*Resolution:\*\* Used `webrtcvad-wheels` (pre-compiled binary) and `rhasspy-silence --no-deps`  

\*\*Impact:\*\* Learned to identify when pre-built alternatives exist for complex dependencies



---



\### Issue #3: API Version Mismatch

\*\*Error:\*\* `ImportError: cannot import name 'Deepgram'` followed by `401 Unauthorized`  

\*\*Cause:\*\* Code written for Deepgram SDK v0.x, attempted installation of v2.12+  

\*\*Resolution:\*\* 

\- Downgraded to `deepgram-sdk==0.3.0`

\- Generated fresh API credentials from correct project scope

\*\*Impact:\*\* Reinforced need to match documentation versions with installed packages



---



\### Issue #4: API Rate Limiting

\*\*Error:\*\* `openai.RateLimitError: 429 - insufficient\_quota`  

\*\*Cause:\*\* OpenAI free tier credits exhausted  

\*\*Resolution:\*\* Migrated to Groq API (free tier, Llama 3.3 70B model)  

\*\*Benefits:\*\* 

\- Zero cost

\- Faster inference (0.3-0.5s vs 1-2s)

\- API-compatible interface minimized code changes



---



\### Issue #5: Breaking Changes in ElevenLabs SDK

\*\*Error:\*\* `AttributeError: 'ElevenLabs' object has no attribute 'generate'`  

\*\*Cause:\*\* ElevenLabs SDK v2.0+ restructured API interface  

\*\*Resolution:\*\* Updated initialization and method calls:

```python

\# Before

elevenlabs.set\_api\_key(key)

audio = elevenlabs.generate(text=response, voice="Adam")



\# After

client = ElevenLabs(api\_key=key)

audio = client.text\_to\_speech.convert(

&nbsp;   text=response,

&nbsp;   voice\_id="pNInz6obpgDQGcFmaJgB",

&nbsp;   model\_id="eleven\_monolingual\_v1"

)

```



---



\### Issue #6: Silent Failure Loop

\*\*Error:\*\* Application continued listening without providing audio responses  

\*\*Cause:\*\* ElevenLabs API call failing without raising exceptions  

\*\*Resolution:\*\* Implemented comprehensive error handling with try-except blocks and logging  

\*\*Impact:\*\* Emphasized importance of defensive programming for external service dependencies



---



\## 🔧 Technical Decisions \& Rationale



\### Groq vs OpenAI

\*\*Decision:\*\* Use Groq API instead of OpenAI  

\*\*Reasoning:\*\*

\- Cost: $0 vs pay-per-token

\- Performance: Comparable quality with Llama 3.3 70B

\- Speed: Faster inference times

\- Compatibility: Drop-in replacement for OpenAI client



\### Legacy SDK Version

\*\*Decision:\*\* Maintain Deepgram SDK v0.3.0 instead of migrating to v2.0+  

\*\*Reasoning:\*\*

\- Significant refactoring required for migration

\- Current version fully functional

\- Focus resources on feature development rather than migration



\### Command Routing Architecture

\*\*Decision:\*\* Implement local command processing before LLM inference  

\*\*Reasoning:\*\*

\- Performance: Instant responses for deterministic queries

\- Cost efficiency: Reduced API call volume

\- Reliability: No dependency on external services for simple commands

\- User experience: Predictable behavior for common tasks



---



\## 📊 Project Metrics

| Metric | Value |

|--------|-------|

| Development Time | ~10 hours |

| Issues Resolved | 15+ |

| APIs Integrated | 3 |

| Total Code Lines | ~280 |

| Dependencies Managed | 50+ |

| Cost | $0 (free tier APIs) |



---



\## 🚀 Implemented Features



\### Core Functionality

\- ✅ Voice input processing (Deepgram)

\- ✅ Natural language understanding (Groq/Llama 3.3)

\- ✅ Voice synthesis (ElevenLabs)

\- ✅ Continuous conversation loop

\- ✅ Error handling and logging



\### Custom Enhancements

\- ✅ Assistant rebranding (JARVIS → IRIS)

\- ✅ Personality customization (humble, approachable tone)

\- ✅ Local command routing system

\- ✅ System automation (10+ commands):

&nbsp; - Time/date queries

&nbsp; - Application launching

&nbsp; - Web search integration

&nbsp; - YouTube playback

&nbsp; - Random utilities (coin flip, dice roll)



---



\## 💡 Key Takeaways



1\. \*\*Version Management:\*\* Always verify compatibility requirements before installation

2\. \*\*API Economics:\*\* Free alternatives often exist with comparable quality

3\. \*\*Error Interpretation:\*\* Stack traces provide specific guidance for resolution

4\. \*\*Documentation Hygiene:\*\* Match documentation version to installed packages

5\. \*\*Optimization Strategy:\*\* Local processing reduces latency and costs

6\. \*\*Open Source Ethics:\*\* Forking with substantial customization demonstrates learning



---



\## 🎯 Planned Enhancements

\- \[ ] Persistent user memory system (JSON-based storage)

\- \[ ] Voice-controlled code generation

\- \[ ] Sentiment analysis for adaptive responses

\- \[ ] Interrupt-driven conversation flow

\- \[ ] Multi-language support

\- \[ ] Enhanced web dashboard with real-time visualizations



---



This development log documents the complete journey from initial setup challenges through to a fully functional, customized voice assistant with production-ready error handling and system integration capabilities.

