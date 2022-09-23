import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
     engine.say(text)
     engine.runAndWait()


def take_command():
    try:
        with sr.Microphone(device_index=0) as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'vaishu' in command:
                command = command.replace('vaishu','')
                print(command)
    except:
        pass
    return command

def run_vaishu():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('current time is' + time)

    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,3)
        talk(info)
        print(info)

    elif 'i love you' in command:
        talk('I love you too ,boss')


    elif 'tell about me' in command:
        talk('you are my lovely boss')

    elif 'do you know god' in command:
        talk('yes, i know , god ia one who created us , and i was created by rubesh so i know gob')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('please say the command again boss')

while True:
    run_vaishu()