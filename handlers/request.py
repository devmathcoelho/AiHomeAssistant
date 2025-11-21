from deepgram import DeepgramClient

import os
import dotenv 
dotenv.load_dotenv()

def SpeechToText(audio_file: str) -> str:
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
    targetAudio = audio_file if audio_file else "quepena"
    AUDIO_PATH = f"audios/{targetAudio}.mp3"

    try:
        deepgram: DeepgramClient = DeepgramClient(api_key=DEEPGRAM_API_KEY)

        with open(AUDIO_PATH, "rb") as audio_file:
            response = deepgram.listen.v1.media.transcribe_file(
                request=audio_file.read(),
                model="nova-3",
                smart_format=True,
            )

        transcript_text = response.results.channels[0].alternatives[0].transcript
        return transcript_text

    except Exception as e:
        print(f"Exception: {e}")

def TextToSpeech(userText: str):
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

    try:
        deepgram: DeepgramClient = DeepgramClient(api_key=DEEPGRAM_API_KEY)

        response = deepgram.speak.v1.audio.generate(
            text=userText,
            model="aura-2-thalia-en"
        )

        output_folder = "responses"
        filename = "test.mp3"

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        file_path = os.path.join(output_folder, filename)

        with open(file_path, "wb") as audio_file:
            with open(file_path, "wb") as audio_file:
                for chunk in response:
                    if chunk: # Ensure the chunk is not empty
                        audio_file.write(chunk)

        print(f"Audio saved to {file_path}")

    except Exception as e:
        print(f"Exception: {e}")