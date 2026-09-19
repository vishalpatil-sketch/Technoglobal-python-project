import pyttsx3
import speech_recognition as sr

class VoiceAssistant:
    def __init__(self):
        self.tts_engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text: str):
        """Converts text response to voice output."""
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen(self) -> str:
        """Captures voice input from the microphone and converts to text."""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio)
                return text
            except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
                return ""
