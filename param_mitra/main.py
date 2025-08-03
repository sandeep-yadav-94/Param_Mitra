import speech_recognition as sr
import pyttsx3
from run_ollama import run_gpt4all

engine = pyttsx3.init()
recognizer = sr.Recognizer()

print("🎙 Listening...")

while True:
    with sr.Microphone() as source:
        print("\n🗣 Speak:")
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            print("🧍 You said:", query)

            response = run_gpt4all(query)
            print("🤖 AI:", response)

            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("😶 Could not understand audio.")
        except sr.RequestError as e:
            print(f"⚠ Could not request results; {e}")