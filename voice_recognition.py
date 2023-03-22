#I have 2 methods in mind. 1 is to activate voice recognition through button, the other (2) is through taking the robot name, proposedly DAVis
import speech_recognition as sr
from pynput.keyboard import Key, Listener
import time 
import threading
#We require threading too run the program, voice recogniser and key_press detector simultaniously
 



#Defining flags
voice_recording_flag = threading.Event()
terminate_program_key = 'q'
program_terminate_flag = threading.Event()
key_register_flag = threading.Event()
key_register_flag.set()


#Detecting record button and program termination button

#Sub functions
def press(key):
    print('1', key)
    if voice_recording_flag.is_set() is False:
        if key_register_flag.is_set():
            print('2', key)
            if key == Key.media_play_pause:
                key_register_flag.clear()
                print('Recording on')
                voice_recording_flag.set()
def release(key):
    if 'char' in dir(key): #Since not all keys are charecter associated, check if the key has a charecter attribute, saved as 'char' in it's attribute dictionary
        if key.char == terminate_program_key: #NOTE: char is not a method, it's an attribute so no char(), only char
            print('\nQUIT\n')
            program_terminate_flag.set()
            return False

#Main Detection function
def detect_record_button_press():
    with Listener(on_press=press, on_release=release) as key_press_detector:
        key_press_detector.join()


#Initializing VR
recognizer = sr.Recognizer()

def convert_speech_to_text():
    try:
        with sr.Microphone(2) as mic: #set pic as a source
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
        print(text)
        # print('Recording over')
        # key_register_flag.set()
        # print(key_register_flag.is_set())
        voice_recording_flag.clear()

def main_program():
    
    while True:
        if program_terminate_flag.is_set():
            break
        while voice_recording_flag.is_set():
            # print(key_register_flag.is_set())
            # key_register_flag.clear()
            # voice_recording_flag.clear()
            convert_speech_to_text()
            if voice_recording_flag.is_set() is False:
                key_register_flag.set()
                pass
        

# print(voice_recording_flag.is_set())
threading.Thread(target=main_program).start()
threading.Thread(target=detect_record_button_press).start()



# def reset():
#     #Defining flags
#     voice_recording_flag = threading.Event()
#     terminate_program_key = 'q'
#     program_terminate_flag = threading.Event()
#     key_register_flag = threading.Event()
#     key_register_flag.set()

#     main_thread = threading.Thread(target=main_program)
#     secondary_thread = threading.Thread(target=detect_record_button_press)
#     main_thread.start()
#     secondary_thread.start()

