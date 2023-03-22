from pynput.keyboard import Key, Listener
def press(key):
    pass
    print(key)
def release(key):
    # print(key)
    if key == Key.space:
        return False #Returns False to stop the listener
##If spacebar is pressed it will stop
with Listener(
        on_press=press,
        on_release=release) as listener:
    listener.join()    
 

import keyboard

# while True:
#     print(keyboard.read_event())

print(keyboard.read_event())

# import time

# print(time.asctime())

