
Sure, here is a revised version:

This repository contains the complete code and files for the Robotics Project I created in 11th grade for the Robotics Workshop at my school.
This Robot was capable of Understanding Low level commands and Talking back to the user via a Speaker.

The project is divided into two main parts:

PC Part:

-> This part handles transcribing voice commands, processing the input, and determining the actions to be taken (such as generating speech responses and controlling movement).
-> The processed information is then instantly transmitted to the Speaker and the Arduino via Bluetooth.
-> This part primarily involves Python scripts.


Arduino Part:

-> The main file for this part is Arduino_Bluetooth_Comm/Arduino_Bluetooth_Comm.ino.
-> It receives messages from the PC through the Bluetooth Module after the PC has processed the commands.
-> The received messages are then translated into mechanical movements by the Arduino such as Moving forward, Turning Right, etc.

The PC worked as a backend, bringing together everything from the mic, speaker and arduino board.
