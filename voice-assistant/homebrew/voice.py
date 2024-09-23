import speech_recognition as aa 
import pywhatkit
import pyttsx3
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait() 

def input_instruction():
    instruction = ""  # Initialize instruction to ensure it's defined
    try:
        with aa.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)  # Fixed 'recognize_goggle' to 'recognize_google'
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', ' ')
                print(instruction)
    except Exception as e: 
        print("Error: ", e)  # Optional: print the error for debugging
        pass
    return instruction

def play_Jarvis():
    instruction = input_instruction()  # Call the function correctly
    print(instruction)
    
    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time' + time)

    elif "date" in instruction:
        date = datetime.datetime.now().strftime('%d %m %Y')
        talk("Today's date" + date)  # Fixed 'time' to 'date'
    
    elif "how are you" in instruction:
        talk("I am fine, what about you")

    elif "whats your name" in instruction:
        talk("I am XXX, What can I do for you?")

    elif "who is" in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    
    else:
        talk("Please repeat.")

play_Jarvis()
