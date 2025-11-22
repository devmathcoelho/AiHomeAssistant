import asyncio

from handlers.TTS_requests import SpeechToText, TextToSpeech
from handlers.MicRecorder import RecordAudio
from handlers.OpenRouter_requests import AsyncOpenRouter

def main ():
    print("Listening...")

    inputResponse = input("Press 1 to record the audio...")

    if inputResponse == "1":
        RecordAudio()
        user_said = SpeechToText("record")

        if user_said is not None:
            print(f"User said: {user_said}")

            TextToSpeech("carregando a resposta da IA...")
            ai_response = asyncio.run(AsyncOpenRouter(user_said))

            if "error" in ai_response.lower():
                print("There was an error getting a response from the AI.")
                return
            
            print(f"AI Response: {ai_response}")
            TextToSpeech(ai_response)
        else:
            print("I couldn't hear anything.")

if __name__ == "__main__":
    main()