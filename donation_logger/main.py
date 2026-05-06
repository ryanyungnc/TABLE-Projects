# Activate virtual enviornment before running:
#   python3 -m venv .venv
#   source .venv/bin/activate   (Mac/Linux)
#   .venv/Scripts/activate      (Windows)
#
# Install Dependancies:
#
# Run:
#   python3 main.py
import sounddevice as sd
import wavio as wv
import numpy as np
import json
import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

#Global variables
FREQ = 44100
MAX_DURATION = 60

def record_input():
    """
    Records audio until user hits enter. 
    Returns the str filename of the saved .wav file.
    """

    chunks = []

    def callback(indata, frames, time, status):
        #Called automatically every time a new audio chunk is ready
        chunks.append(indata.copy())

    filename = f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"

    print("Recording... press Enter to stop.")
    with sd.InputStream(samplerate=FREQ, channels=1, callback=callback):
        input()

    recording = np.concatenate(chunks, axis=0)
    wv.write(filename, recording, FREQ, sampwidth=2)

    return filename

def convert_audio(filename):
    """Takes audio file and passes it into OpenAI's Whisper to convert it to text."""
    with open(filename, "rb") as audio_file:
        response = client.audio.transcriptions.create(model="gpt-4o-transcribe", file=audio_file)

    return response.text

def create_data():
    """Takes transcript and runs it through ChatGPT outputting a JSON object."""
    return null

def input_data():
    return null

if __name__ == "__main__":
    input_audio = record_input()
    print(convert_audio(input_audio))