def say(text):
    name = "Cortana"
    print(f"{name}: {text}")
    
wake_command = "Hello My Baby"   # command to wake it.
goodbye_command = "Goodbye Baby" # command to shutdown it.
open_calc_cmd = "Open Calculator" #command to open calculator
open_notepad_cmd = "Open Notepad" # command

while True:
    mic_input = input("Your command: ")
    if wake_command in mic_input:
        say("Welcome! I am your My Baby!") 
    elif goodbye_command in mic_input:
        say("Goodbye master!")
        exit()
    elif open_calc_cmd in mic_input:
        say("Opening calculator...")
    elif open_notepad_cmd in mic_input:
        say("Opening notepad...")
    else:
        say("Waiting for you..")
    print("")