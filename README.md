This repository contains the complete code and files for the Robotics Project I created in 11th grade for the Robotics Workshop at my school.
This Robot was capable of Understanding Low level commands, Talking back to the user via a Speaker while also being able to Move Based on user inputs through SPEECH and KEY-PRESS.

-------------------------

_The project is divided into two main parts:_

----------------
***PC Part:***

-> This part handles transcribing voice commands, processing the input, and determining the actions to be taken (such as generating speech responses and controlling movement).

-> The processed information is then instantly transmitted to the Speaker and the Arduino via Bluetooth.

-> This part primarily involves Python scripts.

----------------
***Arduino Part:***

-> The main file for this part is Arduino_Bluetooth_Comm/Arduino_Bluetooth_Comm.ino.

-> It receives messages from the PC through the Bluetooth Module after the PC has processed the commands.

-> The received messages are then translated into mechanical movements by the Arduino such as Moving forward, Turning Right, etc.

----
"The PC functioned as a backend, seamlessly integrating the mic, speaker, and Arduino board to bring the Robot to life."
--
