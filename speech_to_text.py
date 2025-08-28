import speech_recognition as sr

def speech_to_text():
        # Initialize recognizer
        r = sr.Recognizer()

        # Use the microphone as a source for input
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)  # Listen to the microphone input

        try:
            # Use Google's free speech recognition service
            voice_data = ""
            voice_data = r.recognize_google(audio)
            print("You said: " + voice_data)
            return voice_data

        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError:
            print("Sorry, the service is unavailable at the moment.")


speech_to_text()