# DAVIS Robotics Project
This repository contains the complete code and files for DAVIS, a robotics project I created in 11th grade for the Robotics Workshop at my school. DAVIS is a robot capable of understanding low-level commands and communicating back to the user via a speaker. It can also move based on user inputs through speech and key-press.

---

_The project is divided into two main parts:_

### Laptop Component
  - **Functionality**: This part handles transcribing voice commands, processing the input, and determining the actions to be taken, such as generating speech responses and controlling movement.
  
  - **Operation**: The processed information is instantly transmitted to the speaker and the Arduino via Bluetooth.
  
  - **Technology**: This component primarily involves Python scripts.

  > --- 
### Arduino Component
  - **Main File**: The key file for this part is Arduino_Bluetooth_Comm/Arduino_Bluetooth_Comm.ino.
  
  - **Operation**: It receives messages from the laptop through the Bluetooth module after the commands have been processed.
  
  - **Functionality**: The received messages are then translated into mechanical movements by the Arduino, such as moving forward, turning right, etc.
  
##### "The laptop functioned as a backend, seamlessly integrating the microphone, speaker, and Arduino board to bring the robot to life."
