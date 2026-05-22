import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_user_input():
    return input("You: ")
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        user_input = get_user_input()
        if user_input.lower() in ["exit", "quit"]:
            speak("Goodbye! Have a great day!")
            break
        else:
            response = f"You said: {user_input}"
            print(response)
            speak(response)