from handlers.TTS_requests import SpeechToText, TextToSpeech
from handlers.MicRecorder import RecordAudio

def main ():
    print("Listening...")

    inputResponse = input("Press 1 to record the audio...")

    if inputResponse == "1":
        RecordAudio()
        user_said = SpeechToText("record")
        TextToSpeech(user_said)
        
    if user_said:
        print(f"User said: {user_said}")
    else:
        print("I couldn't hear anything.")

if __name__ == "__main__":
    main()