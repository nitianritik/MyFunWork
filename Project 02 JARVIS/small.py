import speech_recognition as sr

# create a Recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    print("Speak now...")
    # listen for speech and store it as audio data
    audio_data = r.listen(source)
    print("Processing...")

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio_data)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
