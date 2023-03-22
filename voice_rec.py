import keyboard
from pyparsing import Forward
import speech_recognition as sr
from robot_ai import respond_to_text
from bluetooth import *
from text_to_speech_test import play_text
from time import sleep

mic_on_keys = ['play/pause', 'r']
cheat_codes = {
    'w' : "Forward",
    'x' : "Backward",
    'a' : "Left",
    'd' : "Right",
    's' : "Stop"
 }

# forward_flag = False
# backward_flag = False
# right_flag = False
# left_flag = False

# forward_keys = ['w', 'up']
# backward_keys = ['s', 'down']
# right_keys = ['d', 'right']
# left_keys = ['a', 'left']
# move_keys = []
# move_keys_dict = {}
# # move_key_flags = {}
# for keys in [forward_keys, backward_keys, right_keys, left_keys]:
#     for key in keys:
#         move_keys.append(key)
# for key in forward_keys:
#     move_keys_dict[key] = "Forward"
#     # move_key_flags[key] = forward_flag
# for key in backward_keys:
#     move_keys_dict[key] = "Backward"
#     # move_key_flags[key] = backward_flag
# for key in right_keys:
#     move_keys_dict[key] = "Right"
#     # move_key_flags[key] = right_flag
# for key in left_keys:
#     move_keys_dict[key] = "Left"
#     # move_key_flags[key] = left_flag


#Defining Movement Commands
mechanical_commands = {
    'right' : "Right",
    'android' : "Right",
    'left' : "Left",
    'download' : "Left",
    'forward' : "Forward",
    'front' : "Forward",
    'covid' : "Forward",
    'back' : "Backward",
    'backward' : "Backward",
    'backwards' : "Backward",
    'barcode' : "Backward",
    'reset' : "Reset",
    'stop': "Stop",
    'top' : "Stop",
    'hault' : "Stop"
    }

command_list = mechanical_commands.keys()




#Initializing VR and bluetooth
recognizer = sr.Recognizer()
bluetooth = Bluetooth()


def record_and_convert():
    try:
        with sr.Microphone(1) as mic: #set pic as a source
            recognizer.adjust_for_ambient_noise(mic, 0.5) #Stop recording when speech is over

            #Recieve an input
            audio = recognizer.listen(mic)#recieve from source

            #Covert input into text
            text = recognizer.recognize_google(audio)#Use google api
            text = text.lower() #Turn everything into lowercase
    except:
        pass
    
    else:
        # print(key_register_flag.is_set())
        return text
        # print('Recording over')
        # key_register_flag.set()
        # print(key_register_flag.is_set())
        # voice_recording_flag.clear()

def detect_key():
    event = str(keyboard.read_event()).split('(')[1].rstrip(')')
    key = event.split()[0]
    key_movement = event.split()[-1]

    return [key, key_movement]


while True:

    command_flag = False

    event = detect_key()
    # print(event)


    if event[1] == 'down':
        # print('press check')
        if event[0].lower() in mic_on_keys:
            text = ''
            print('...Recording...')
            while text == '' or text == None:
                text = record_and_convert()

            words_in_text = text.split()
            print(text)
            print('Recording over')

            if 'abort' in text or 'terminate' in text or 'quit' in text:
                break

            #Connect to bluetooth
            if 'connect' in words_in_text:
                play_text(bluetooth.connect_to_bluetooth())
            if 'disconnect' in words_in_text:
                bluetooth.disconnect_bluetooth()

            for command in command_list:
                if command in text:
                    if bluetooth.connected_flag:
                        bluetooth.communicate(mechanical_commands[command])
                        command_flag = True
                    else:
                        play_text("Please connect to bluetooth first.")
            if command_flag is False:
                respond_to_text(text)
        
        elif event[0] in cheat_codes.keys():
            sleep(1.5)
            bluetooth.communicate(cheat_codes[event[0]])

    #Move from Arrow Keys
   #if event[1] == 'down':
        # elif event[0] in move_keys:
        #     command = move_keys_dict[event[0]]
        #     if command == "Forward":
        #         if forward_flag is False:
        #             forward_flag = True
        #             bluetooth.communicate(command)
        #     if command == "Backward":
        #         if backward_flag is False:
        #             backward_flag = True
        #             bluetooth.communicate(command)
        #     if command == "Right":
        #         if right_flag is False:
        #             right_flag = True
        #             bluetooth.communicate(command)
        #     if command == "Left":
        #         if left_flag is False:
        #             left_flag = True
        #             bluetooth.communicate(command)

    # elif event[1] == 'up':
    #     if event[0] in move_keys:
    #         command = move_keys_dict[event[0]]
    #         if command == "Forward":
    #             if forward_flag is False:
    #                 forward_flag = True
    #                 bluetooth.communicate(command)
    #         if command == "Backward":
    #             if backward_flag is False:
    #                 backward_flag = True
    #                 bluetooth.communicate(command)
    #         if command == "Right":
    #             if right_flag is False:
    #                 right_flag = True
    #                 bluetooth.communicate(command)
    #         if command == "Left":
    #             if left_flag is False:
    #                 left_flag = True
    #                 bluetooth.communicate(command)
            




        elif event[0] == 'q':
            break
    


