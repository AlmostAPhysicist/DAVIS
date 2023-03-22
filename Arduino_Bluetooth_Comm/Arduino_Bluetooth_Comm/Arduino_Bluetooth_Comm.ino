#include "SoftwareSerial.h"

//setting up bluetooth software serial info
//NOTE: this is Software serial, not serial! so we're using normal pwm pins
int recievePin = 6;
int transmitPin = 10;
SoftwareSerial serial_connection(transmitPin, recievePin);

//Defining data transfer size...
#define BUFFER_SIZE 64;
char inData[BUFFER_SIZE];
char inChar =- 1;
int count = 0;
int i = 0;




void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  serial_connection.begin(9600);
  serial_connection.println("...Ready...");
  Serial.println("Stared");

}

void loop() {
  // put your main code here, to run repeatedly:

  //Setting up recieve settings related to bytes, preventing Buffer Overruns
  byte byte_count = serial_connection.available();
  if(byte_count) {
    Serial.println("Incoming Data");
    int first_bytes = byte_count;
    in remaining_bytes = 0;
    if(first_bytes >= BUFFER_SIZE-1){
      remaining_bytes = byte_count - (BUFFER_SIZE - 1);
    }


    //Store bytes as long as they are under the BUFFER_SIZE
    for(i=0; i<first_bytes; i++){
      inChar = serial_connection.read();
      inData[i] = inChar
    }
    inData[i] = '\0';


    //Burn off any of the remaining bytes
    for(i=0; i<remaining_bytes; i++){
      inChar = serial_connection.read();
    }


    Serial.println(inData);
    serial_connection.println("Hello from Bluetooth" + String(count));
    count ++
  }
  
}
