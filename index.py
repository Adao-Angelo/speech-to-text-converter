import speech_recognition as sr


def recognize_speech():
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Hello!")
        audio = microphone.listen(source)
        try:
            phrase = microphone.recognize_google(audio,language="pt-BR")
            print("you speak -> " + phrase)
        except :
            print("Google Speech Recognition could not understand audio")
        return phrase

recognize_speech()