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
context = "You are Iris, a humble and approachable AI assistant. You are friendly, helpful, and speak naturally like a supportive friend. Keep your answers brief and easy to understand, limited to 1-2 short sentences."
conversation = {"Conversation": []}
RECORDING_PATH = "audio/recording.wav"


def request_gpt(prompt: str) -> str:
    """
    Send a prompt to the Groq API and return the response.

    Args:
        - state: The current state of the app.
        - prompt: The prompt to send to the API.

    Returns:
        The response from the API.
    """
    response = gpt_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content


async def transcribe(
    file_name: Union[Union[str, bytes, PathLike[str], PathLike[bytes]], int]
):
    """
    Transcribe audio using Deepgram API.

    Args:
        - file_name: The name of the file to transcribe.

    Returns:
        The response from the API.
    """
    with open(file_name, "rb") as audio:
        source = {"buffer": audio, "mimetype": "audio/wav"}
        response = await deepgram.transcription.prerecorded(source)
        return response["results"]["channels"][0]["alternatives"][0]["words"]


def log(log: str):
    """
    Print and write to status.txt
    """
    print(log)
    with open("status.txt", "w") as f:
        f.write(log)


def handle_local_commands(text: str) -> tuple[bool, str]:
    """
    Check if the user input is a local command and handle it.
    Returns (handled: bool, response: str)
    """
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
    if "open chrome" in text_lower:
        try:
            if platform.system() == "Windows":
               os.startfile("chrome")
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", "-a", "Google Chrome"])
            else:  # Linux
                subprocess.Popen(["google-chrome"])
            return True, "Opening Chrome for you"
        except:
            return True, "Sorry, I couldn't open Chrome"
    
    # Open VSCode
    if "open vscode" in text_lower or "open vs code" in text_lower or "open visual studio code" in text_lower:
        try:
            if platform.system() == "Windows":
                subprocess.Popen(["code"])
            else:
                subprocess.Popen(["code"])
            return True, "Opening VS Code"
        except:
            return True, "Sorry, I couldn't open VS Code"
    
    # Open Spotify
    if "open spotify" in text_lower:
        try:
            if platform.system() == "Windows":
                subprocess.Popen(["spotify.exe"])
            else:
                subprocess.Popen(["open", "-a", "Spotify"])
            return True, "Opening Spotify"
        except:
            return True, "Sorry, I couldn't open Spotify"
    
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


if __name__ == "__main__":
    while True:
        # Record audio
        log("Listening...")
        speech_to_text()
        log("Done listening")

        # Transcribe audio
        current_time = time()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        words = loop.run_until_complete(transcribe(RECORDING_PATH))
        string_words = " ".join(
            word_dict.get("word") for word_dict in words if "word" in word_dict
        )
        with open("conv.txt", "a") as f:
            f.write(f"{string_words}\n")
        transcription_time = time() - current_time
        log(f"Finished transcribing in {transcription_time:.2f} seconds.")


        # Check if it's a local command first
        is_local_command, local_response = handle_local_commands(string_words)
        
        if is_local_command:
            response = local_response
            log("Handled as local command")
        else:
            # Get response from Groq
            current_time = time()
            context += f"\nUser: {string_words}\nIris: "
            response = request_gpt(context)
            context += response
            gpt_time = time() - current_time
            log(f"Finished generating response in {gpt_time:.2f} seconds.")        

        # Convert response to audio using ElevenLabs
        current_time = time()
        try:
            audio_generator = elevenlabs_client.text_to_speech.convert(
                text=response,
                voice_id="pNInz6obpgDQGcFmaJgB",  # Adam voice
                model_id="eleven_monolingual_v1"
            )
            
            # Save audio to file
            with open("audio/response.wav", "wb") as f:
                for chunk in audio_generator:
                    f.write(chunk)
            
            audio_time = time() - current_time
            log(f"Finished generating audio in {audio_time:.2f} seconds.")
        except Exception as e:
            log(f"Error generating audio: {e}")
            continue

        # Play response
        log("Speaking...")
        sound = mixer.Sound("audio/response.wav")
        # Add response as a new line to conv.txt
        with open("conv.txt", "a") as f:
            f.write(f"{response}\n")
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))
        print(f"\n --- USER: {string_words}\n --- IRIS: {response}\n")