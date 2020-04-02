from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")

speak.Speak("Hii this is sagar gupta from terna engineering college")