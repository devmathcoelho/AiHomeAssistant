from handlers.request import SpeechToText, TextToSpeech

def main ():
    print("Listening...")
    user_said = SpeechToText("quepena")
    TextToSpeech("Olá! Como posso ajudar?")
    
    if user_said:
        print(f"User said: {user_said}")
    else:
        print("I couldn't hear anything.")

if __name__ == "__main__":
    main()