
import speech_recognition as sr

AUDIO_FILE = ("your_file.wav")
#use audio file as source

r = sr.Recognizer() #initialize the recognizer

with sr.AudioFile(AUDIO_FILE) as source:
    
    audio = r.record(source)
    #reads the audio file
    
try:
    print("Audio file contains " + r.recognize_google(audio))
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    
except sr.RequestError:
    print("couldn't get the results from Google Speech Recognition")
