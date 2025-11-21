import os
import dotenv
dotenv.load_dotenv()

from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

def SpeechToText(audio_file: str) -> str:
    ELVENLABS_API_KEY = os.getenv("ELVENLABS_API_KEY")

    if not ELVENLABS_API_KEY:
        print("Error: ELVENLABS_API_KEY environment variable not set.")
        return ""
    
    targetAudio = audio_file if audio_file else "quepena"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    AUDIO_PATH = os.path.join(parent_dir, "responses", f"{targetAudio}.mp3")
    
    # Print the path for debugging
    # print(f"Attempting to open file at: {AUDIO_PATH}")
    
    try:
        # Check if the file exists before opening to get a clearer error
        if not os.path.exists(AUDIO_PATH):
            print(f"Error: File not found at path: {AUDIO_PATH}")
            return "File Not Found Error"
    except Exception as e:
        print(f"Exception while checking file existence: {e}")
        return "File Existence Check Error"

    elevenlabs = ElevenLabs(api_key=ELVENLABS_API_KEY)

    try:
        with open(AUDIO_PATH, "rb") as audio_file_object:
            transcription = elevenlabs.speech_to_text.convert(
                file=audio_file_object,  # Pass the opened file object directly
                model_id="scribe_v1",
                tag_audio_events=True,
                diarize=True
                )
            
        return transcription.text
    
    except Exception as e:
        print(f"Exception during transcription: {e}")

def TextToSpeech(userText: str):
    ELVENLABS_API_KEY = os.getenv("ELVENLABS_API_KEY")

    try:
        elevenlabs = ElevenLabs(api_key=ELVENLABS_API_KEY)

        audio = elevenlabs.text_to_speech.convert(
            text=userText,
            voice_id="UgBBYS2sOqTuMpoF3BR0",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        play(audio)

    except Exception as e:
        print(f"Exception: {e}")