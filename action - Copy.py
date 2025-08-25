import datetime
import webbrowser
import speech_to_text
import text_to_speech

def Action(data):
    user_data = data.lower()


    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Nomaan's virtual assistant")
        return "My name is Nomaan's virtual assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("Hey, sir! How can I help you?")
        return "Hey, sir! How can I help you?"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning, sir")
        return "Good morning, sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        time_str = f"Hour: {current_time.hour}, Minute: {current_time.minute}"
        
        # Assuming text_to_speech is a function from a library/module
        text_to_speech.text_to_speech(time_str)
        
        return time_str

    elif "are you listening to me" in user_data:
        text_to_speech.text_to_speech("Yes sir, I'm listening")
        return "Yes sir, I'm listening"

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okay sir")
        return "Okay sir"

    elif "ky kushagra sabse bada wala paagal hai" in user_data:
        text_to_speech.text_to_speech("haa na kushagra  sabse bada wali paagaal hai!!!")
        return "haa na kushagra sabse bada wala paagaal h!!!"

    elif "kushagra sach me paagal hai naa" in user_data:
        text_to_speech.text_to_speech("haa kushagra sachhhh me paaagaal hai")
        return "haa kushagra saccchhh me paaagaal hai"

    elif "play naat" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is ready for you")
        return "youtube.com is ready for you"

    elif "hesham dob" in user_data:
        text_to_speech.text_to_speech("5th february")
        return "5th february"

    elif "play music" in user_data:
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("spotify.com is ready for you")
        return "spotify.com is ready for you"

    elif "show cricket score" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("google.com is ready for you")
        return "google.com is ready for you"

    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"

