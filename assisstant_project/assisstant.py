
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import random

# Create speech engine
engine = pyttsx3.init()

# Set speaking speed
engine.setProperty("rate", 150)


def speak(text):
    """Speak the given text."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the user's voice and convert it to text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I did not hear anything.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand your voice.")
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""


def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)


def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why did the computer go to the doctor? Because it had a virus.",
        "Why was the computer cold? Because it left its Windows open.",
        "What do you call a computer that sings? A Dell."
    ]

    speak(random.choice(jokes))


def open_website(command):
    """Open common websites."""
    
    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    else:
        speak("I do not know that website.")


def open_application(command):
    """Open common Windows applications."""

    if "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "command prompt" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")

    else:
        speak("I cannot open that application yet.")


def save_note():
    """Take a voice note and save it to a file."""

    speak("What should I write in the note?")

    note = listen()

    if note:
        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        speak("Your note has been saved.")


def show_help():
    """Display supported commands."""

    print("\n----- SUPPORTED COMMANDS -----")
    print("1. What is the time")
    print("2. Open YouTube")
    print("3. Open Google")
    print("4. Open GitHub")
    print("5. Open LinkedIn")
    print("6. Open Notepad")
    print("7. Open Calculator")
    print("8. Tell me a joke")
    print("9. Take a note")
    print("10. Help")
    print("11. Exit")
    print("------------------------------\n")

    speak("I can tell the time, open websites and applications, tell jokes, and save notes.")


def process_command(command):
    """Process the user's command."""

    if command == "":
        return True

    # Exit command
    if "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye. Have a nice day.")
        return False

    # Time command
    elif "time" in command:
        tell_time()

    # Joke command
    elif "joke" in command:
        tell_joke()

    # Website commands
    elif "open youtube" in command or "open google" in command \
            or "open github" in command or "open linkedin" in command:
        open_website(command)

    # Application commands
    elif "open notepad" in command \
            or "open calculator" in command \
            or "open command prompt" in command:
        open_application(command)

    # Notes
    elif "take a note" in command or "save a note" in command:
        save_note()

    # Help
    elif "help" in command or "commands" in command:
        show_help()

    else:
        speak("Sorry, I do not know that command.")

    return True


# ---------------- MAIN PROGRAM ----------------

speak("Hello! I am your voice-controlled assistant.")
speak("Say help to hear the available commands.")

running = True

while running:
    command = listen()
    running = process_command(command)
