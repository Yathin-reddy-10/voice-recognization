import speech_recognition as sr
import pyttsx3
import time

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to audio and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust to ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, I couldn't reach the server.")
            return None

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main voice interaction function
def voice_interaction():
    text = listen()  # Listen for input
    if text:  
        # Example response based on recognized speech
        response = f"You said: {text}"  # You can add custom responses or logic
        speak(response)
    else:
        speak("Sorry, I didn't hear anything properly.")

# Trigger the interaction (this is where your program will run continuously)
if __name__ == "__main__":
    while True:
        voice_interaction()  # Keeps interacting in a loop
        print("\nWaiting for next command...")
        time.sleep(1)  # Small delay between commands
