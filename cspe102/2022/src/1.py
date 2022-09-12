wake_word = "Hey Argie"

cmd_calc = "Open Calculator"
cmd_browser = "Open Browser"
cmd_notepad = "Open Notepad"
cmd_bye = "bye"

wake_word_input = input("Enter your wake word: ") # <- INPUT WAKE WORD

if wake_word_input == wake_word:
    print("Welcome master!")
    
    while True:
        command_input = input("Enter your command: ") # <- INPUT COMMAND
        if command_input == cmd_calc:
            print("Opening calculator...")
        elif command_input == cmd_browser:
            print("Opening browser...")
        elif command_input == cmd_notepad:
            print("Opening notepad...")
        elif command_input == cmd_bye:
            print("BYE!")
            break
        else:
            print("Command not found!")
    
