"""Main file for the Jarvis project"""
import os
from os import PathLike
from time import time
import asyncio
import webbrowser
import subprocess
import platform
import json
from datetime import datetime
from typing import Union

from dotenv import load_dotenv
from groq import Groq
from deepgram import Deepgram
import pygame
from pygame import mixer
from elevenlabs.client import ElevenLabs

from record import speech_to_text

# Load API keys
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Initialize APIs
gpt_client = Groq(api_key=GROQ_API_KEY)
deepgram = Deepgram(DEEPGRAM_API_KEY)
elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# mixer is a pygame module for playing audio
mixer.init()

# Change the context if you want to change Iris' personality
context = (
    "You are Iris, a humble and approachable AI assistant. "
    "You are friendly, helpful, and speak naturally like a supportive friend. "
    "Keep your answers brief and easy to understand, limited to 1-2 short sentences."
)
conversation = {"Conversation": []}
RECORDING_PATH = "audio/recording.wav"


def request_gpt(prompt: str) -> str:
    """Send a prompt to the Groq API and return the response."""
    response = gpt_client.chat.completions.create(
        messages=[{"role": "user", "content": f"{prompt}"}],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content


async def transcribe(file_name: Union[Union[str, bytes, PathLike[str], PathLike[bytes]], int]):
    """Transcribe audio using Deepgram API."""
    with open(file_name, "rb") as audio:
        source = {"buffer": audio, "mimetype": "audio/wav"}
        response = await deepgram.transcription.prerecorded(source)
        return response["results"]["channels"][0]["alternatives"][0]["words"]


def log(log_text: str):
    """Print and write to status.txt"""
    print(log_text)
    with open("status.txt", "w") as f:
        f.write(log_text)


def handle_local_commands(text: str) -> tuple[bool, str]:
    """Check if the user input is a local command and handle it."""
    text_lower = text.lower()

    # Time command
    if "what time" in text_lower or "current time" in text_lower:
        current_time = datetime.now().strftime("%I:%M %p")
        return True, f"It's currently {current_time}"

    # Date command
    if "what date" in text_lower or "today's date" in text_lower or "what day" in text_lower:
        current_date = datetime.now().strftime("%B %d, %Y")
        return True, f"Today is {current_date}"

    # Open Chrome
    if "open chrome" in text_lower or "open google chrome" in text_lower:
        try:
            if platform.system() == "Windows":
                try:
                    subprocess.Popen(["chrome"])
                except:
                    try:
                        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
                    except:
                        subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", "-a", "Google Chrome"])
            else:  # Linux
                subprocess.Popen(["google-chrome"])
            return True, "Opening Chrome"
        except Exception as e:
            return True, f"Sorry, I couldn't open Chrome: {e}"

    # Open VSCode
    if "open vscode" in text_lower or "open vs code" in text_lower or "open visual studio code" in text_lower:
        try:
            if platform.system() == "Windows":
                try:
                    subprocess.Popen(["code"])
                except:
                    subprocess.Popen(["C:\\Users\\archa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
            else:
                subprocess.Popen(["code"])
            return True, "Opening VS Code"
        except Exception as e:
            return True, f"Sorry, I couldn't open VS Code: {e}"

    # Open Spotify
    if "open spotify" in text_lower:
        try:
            if platform.system() == "Windows":
                try:
                    subprocess.Popen(["spotify"])
                except:
                    subprocess.Popen(["C:\\Users\\archa\\AppData\\Roaming\\Spotify\\Spotify.exe"])
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", "-a", "Spotify"])
            else:
                subprocess.Popen(["spotify"])
            return True, "Opening Spotify"
        except Exception as e:
            return True, f"Sorry, I couldn't open Spotify: {e}"

    # Search Google
    if "search google for" in text_lower or "google search" in text_lower:
        query = text_lower.split("for")[-1].strip() if "for" in text_lower else text_lower.replace("google search", "").strip()
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)
        return True, f"Searching Google for {query}"

    # Play on YouTube
    if "play" in text_lower and "youtube" in text_lower:
        query = text_lower.replace("play", "").replace("on youtube", "").replace("youtube", "").strip()
        url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        webbrowser.open(url)
        return True, f"Playing {query} on YouTube"

    # Open GitHub
    if "open github" in text_lower or "open my github" in text_lower:
        webbrowser.open("https://github.com")
        return True, "Opening GitHub"

    # Flip coin
    if "flip a coin" in text_lower or "flip coin" in text_lower:
        import random
        result = random.choice(["Heads", "Tails"])
        return True, f"It's {result}!"

    # Roll dice
    if "roll dice" in text_lower or "roll a dice" in text_lower:
        import random
        result = random.randint(1, 6)
        return True, f"You rolled a {result}"

    # No local command found
    return False, ""


# === USER MEMORY FUNCTIONS ===
def load_user_data():
    """Load user data from JSON file."""
    try:
        with open("user_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"name": None, "preferences": {}}


def save_user_data(data):
    """Save user data to JSON file."""
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)


def check_for_name_in_input(text: str, user_data: dict) -> tuple[bool, str, dict]:
    """Check if user is introducing themselves."""
    text_lower = text.lower()

    if any(phrase in text_lower for phrase in ["my name is", "i am", "i'm", "call me"]):
        if "my name is" in text_lower:
            name = text_lower.split("my name is")[-1].strip()
        elif "i am" in text_lower:
            name = text_lower.split("i am")[-1].strip()
        elif "i'm" in text_lower:
            name = text_lower.split("i'm")[-1].strip()
        elif "call me" in text_lower:
            name = text_lower.split("call me")[-1].strip()
        else:
            name = ""

        name = name.split()[0].capitalize() if name else ""
        if name:
            user_data["name"] = name
            save_user_data(user_data)
            return True, f"Nice to meet you, {name}! I'll remember that. How can I help you today?", user_data

    return False, "", user_data


# === MAIN LOOP ===
if __name__ == "__main__":
    # Load user data at startup
    user_data = load_user_data()

    # Greet user by name if known
    if user_data.get("name"):
        print(f"\n👋 Welcome back, {user_data['name']}!\n")
    else:
        print("\n👋 Hello! I'm IRIS. What's your name?\n")

    while True:
        log("Listening...")
        speech_to_text()
        log("Done listening")

        # Transcribe
        current_time = time()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        words = loop.run_until_complete(transcribe(RECORDING_PATH))
        string_words = " ".join(word_dict.get("word") for word_dict in words if "word" in word_dict)
        with open("conv.txt", "a") as f:
            f.write(f"{string_words}\n")

        transcription_time = time() - current_time
        log(f"Finished transcribing in {transcription_time:.2f} seconds.")

        # Check for name introduction
        is_name_intro, name_response, user_data = check_for_name_in_input(string_words, user_data)

        if is_name_intro:
            response = name_response
            log("Learned user's name")
        else:
            # Check local command
            is_local_command, local_response = handle_local_commands(string_words)
            if is_local_command:
                response = local_response
                log("Handled as local command")
            else:
                # Get AI response
                current_time = time()
                if user_data.get("name"):
                    context_with_name = f"You are talking to {user_data['name']}. {context}"
                else:
                    context_with_name = context
                context_with_name += f"\nUser: {string_words}\nIris: "
                response = request_gpt(context_with_name)
                gpt_time = time() - current_time
                log(f"Finished generating response in {gpt_time:.2f} seconds.")

        # Convert response to audio
        current_time = time()
        try:
            audio_generator = elevenlabs_client.text_to_speech.convert(
                text=response,
                voice_id="pNInz6obpgDQGcFmaJgB",
                model_id="eleven_monolingual_v1",
            )
            with open("audio/response.wav", "wb") as f:
                for chunk in audio_generator:
                    f.write(chunk)

            audio_time = time() - current_time
            log(f"Finished generating audio in {audio_time:.2f} seconds.")
        except Exception as e:
            log(f"Error generating audio: {e}")
            continue

        # Play audio
        log("Speaking...")
        sound = mixer.Sound("audio/response.wav")
        with open("conv.txt", "a") as f:
            f.write(f"{response}\n")
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))

        user_display = user_data.get("name", "USER")
        print(f"\n --- {user_display}: {string_words}\n --- IRIS: {response}\n")
