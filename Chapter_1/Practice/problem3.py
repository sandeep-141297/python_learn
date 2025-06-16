#Install an external module and use it to perform an operation of your interest

#pip install pyttsx3
#Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak. - https://pypi.org/project/pyttsx3/

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, I am sandeep and i am begginer in python")
engine.runAndWait()