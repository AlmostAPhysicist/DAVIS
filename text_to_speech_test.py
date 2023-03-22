# from numpy import  insert
import pyttsx3 as tts
import soundfile as sf
import sounddevice as sd
# import time
# This module has 2 parts 
# 1. Making an audio file
# 2. Playing the file through a given device
file_name = 'audio_file_converted.mp3'
def text_to_speech(text, speach_rate=150, speaker_index=1):

    #Initializing speech engine
    narrator = tts.init() #Initializing a speech engine by name narrator
    available_voices = narrator.getProperty('voices') #List of available voices

    #Setting property
    narrator.setProperty('voice', available_voices[speaker_index].id) #Choose Voice Number 2 for female [NOTE: value passed should be the id. therefore .id]
    narrator.setProperty('rate', speach_rate)

    #Saving file
    narrator.save_to_file(text, file_name) #Add to queue
    narrator.runAndWait() #Speak/Save file

def play_on_device(media_file, play_on_system_default=True, device='Speakers (HP Mini 300), MME'):

    #Creating array
    data, samplerate = sf.read(media_file, dtype='float32') #Creating data and frequency information. data holds a numpy array and samplerate hold the information about playspeed (which depends on frequency)

    #Setting playback device
    if play_on_system_default is False:
        sd.default.device = device #'Speakers (HP Mini 300), MME' 

    #Playing the audio file
    sd.wait()
    sd.play(data, samplerate)
    sd.wait()

def play_text(text):
    text_to_speech(text)
    play_on_device(file_name)
# countdown_duration = 7
# text = f"Self Destruct Initiating in T minus {countdown_duration} seconds"
# text_to_speech(text)
# play_on_device(file_name)
# initial_time = time.time()

# # countdown_duration += 1
# seconds_elapsed = 0

# while seconds_elapsed <= countdown_duration:
#     if time.time() > (initial_time+0.1):
#         initial_time += 1
#         file_name = 'audio_file_converted_' + str(text) + '.mp3' 
#         text = countdown_duration - seconds_elapsed
#         text_to_speech(text)
#         play_on_device(file_name)
#         seconds_elapsed += 1


# print(data)


