import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import os
import numpy as np

def RecordAudio():
    # Configuration for the recording
    FS = 44100  # Sample rate (Hz)
    SECONDS = 5 # Duration of recording

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    MP3_FILENAME = os.path.join(parent_dir, "responses", "record.mp3") # Output MP3 file path

    print("⚡️ Your voice will be recorded for 5 seconds!")

    recording = sd.rec(int(SECONDS * FS), samplerate=FS, channels=1, dtype='int16')
    sd.wait() # Wait until recording is finished

    print("🛑 Recording finished. Saving...")

    try:
        temp_wav = "temp_recording.wav"
        write(temp_wav, FS, recording)

        audio_segment = AudioSegment.from_wav(temp_wav)
        audio_segment.export(MP3_FILENAME, format="mp3")

        os.remove(temp_wav)
        
        print(f"✅ Success! Audio saved to {MP3_FILENAME}")

    except Exception as e:
        print(f"🚨 An error happened during file saving: {e}")