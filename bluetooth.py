import serial
import time

class Bluetooth():
    def __init__(self, port='COM6', frequency=9600):
        self.port = port
        self.frequency = frequency
        self.bluetooth = None
        self.connected_flag = False


    def connect_to_bluetooth(self):
        connection_flag = False
        time_of_sending = time.time()
        time_current = time_of_sending
        while connection_flag is False:
            time_current = time.time()
            if time_current > time_of_sending+4:
                break
            try:
                self.bluetooth = serial.Serial(self.port, self.frequency)
            except:
                pass
            else:
                connection_flag = True
                text = "Connected"
                print(text)
                self.connected_flag = True

        if connection_flag is False:
            text = "Unable to Connect to Bluetooth"

        return text

    # print("Start")
    def send_through_bluetooth(self, text):
        # port = 'COM6'
        # bluetooth = serial.Serial(port, 9600)
        # print("Connected")
        self.bluetooth.flushInput()
        text_to_send = bytes(text, 'utf-8')
        self.bluetooth.write(text_to_send)

    def recieve_from_bluetooth(self):
        input_data = self.bluetooth.readline()
        print('message from bluetooth: ' + input_data.decode())
    
    def disconnect_bluetooth(self):
        try:
            self.bluetooth.close()
            self.connected_flag = False
            text = "Disconnected"
            return text
        except:
            pass

        # x = ''
        # while x != 'q':
        #     x = input(': ')
        #     if x == 'o':
        #         bluetooth.write(b"turn on")
        #     else:
        #         bluetooth.write(str.encode(x))

        #     input_data = bluetooth.readline()
        #     print('message from bt: ' + input_data.decode())
        # print('Over')

    def communicate(self, text):
        self.send_through_bluetooth(text)
        self.recieve_from_bluetooth()

    def conn_and_comm(self, text):
        self.connect_to_bluetooth()
        self.send_through_bluetooth(text)
        time_of_sending = time.time()
        time_current = time_of_sending
        while time_current < time_of_sending+4:
            time_current = time.time()
            try:
                self.recieve_from_bluetooth()
            except:
                pass
            else:
                break
    
    def just_once(self, text):
        self.connect_to_bluetooth()
        self.send_through_bluetooth(text)
        time_of_sending = time.time()
        time_current = time_of_sending
        while time_current < time_of_sending+4:
            try:
                self.recieve_from_bluetooth()
            except:
                pass
            else:
                break
        self.disconnect_bluetooth()

# bluetooth = Bluetooth()
# bluetooth.connect_to_bluetooth()
# # print("connected")
# init_time = time.time()
# # while True:
# #     bluetooth.communicate(input(": "))
# while True:
#     current_time = time.time()
#     if current_time > init_time+1:
#         bluetooth.communicate("Forward")
#         # print("right")
#         break
# while True:
#     current_time = time.time()
#     if current_time > init_time+3:
#         bluetooth.communicate("Right")
#         # print("forward")
#         break
# while True:
#     current_time = time.time()
#     if current_time > init_time+4:
#         bluetooth.communicate("Stop")
#         # print("forward right")
#         break
# # while True:
# #     current_time = time.time()
# #     if current_time > init_time+10:
# #         bluetooth.communicate("Left")
# #         # print()
# #         break
# # bluetooth.communicate("Left")
# bluetooth.disconnect_bluetooth()
# # bluetooth.conn_and_comm("Left")

