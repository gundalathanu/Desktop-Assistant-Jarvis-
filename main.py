import pyttsx3,speech_recognition as sr,webbrowser,datetime,os,wikipedia
engine=pyttsx3.init()
def speak(t):
    print("Jarvis:",t);engine.say(t);engine.runAndWait()
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as s:
        print("Listening...")
        r.adjust_for_ambient_noise(s,duration=1)
        a=r.listen(s)
    try:return r.recognize_google(a).lower()
    except:return ""
speak("Hello I am Jarvis")
while True:
    c=listen()
    print("You:",c)
    if "google" in c: webbrowser.open("https://google.com");speak("Opening Google")
    elif "youtube" in c: webbrowser.open("https://youtube.com");speak("Opening YouTube")
    elif "time" in c: speak(datetime.datetime.now().strftime("%I:%M %p"))
    elif "notepad" in c: os.system("notepad")
    elif "who is" in c:
        try:speak(wikipedia.summary(c.replace("who is",""),sentences=2))
        except:speak("No information found")
    elif "exit" in c or "stop" in c:
        speak("Goodbye");break
