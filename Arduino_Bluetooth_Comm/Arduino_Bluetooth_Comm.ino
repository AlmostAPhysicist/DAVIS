#include "SoftwareSerial.h"

//setting up bluetooth software serial info
//NOTE: this is Software serial, not serial! so we're using normal pwm pins
int recievePin = A4;
int transmitPin = A5;
SoftwareSerial serial_connection(transmitPin, recievePin);

//Defining data transfer size...
#define BUFFER_SIZE 64//This will prevent buffer overruns.
char inData[BUFFER_SIZE];//This is a character buffer where the data sent by the python script will go.
char inChar=-1;//Initialie the first character as nothing
int count=0;//This is the number of lines sent in from the python script
int i=0;//Arduinos are not the most capable chips in the world so I just create the looping variable once



//Defining my move functions

#include <AFMotor.h>

int frontRight = 4;
int frontLeft = 1;
int backRight = 3;
int backLeft = 2;
AF_DCMotor rightFront(frontRight);
AF_DCMotor rightBack(backRight);
AF_DCMotor leftFront(frontLeft);
AF_DCMotor leftBack(backLeft);

int speedFactor = 12;
int timeForTurnStationary = 1470;
int timeForTurnMoving = 1500;
int forwardTime = 3000;
int backwardTime = 3000;

int motorSpeedDefault = 10 * speedFactor;
int motorFast = 21 * speedFactor;
int motorSlow = 6 * speedFactor;
int motorTurnSpeed = 20 * speedFactor;

bool carMoving = false;
String text = "";

void resetSpeed(int motorSpeed = motorSpeedDefault) {
  rightFront.setSpeed(motorSpeed);
  rightBack.setSpeed(motorSpeed);
  leftBack.setSpeed(motorSpeed);
  leftFront.setSpeed(motorSpeed);
}

void stopMoving() {
  rightFront.run(RELEASE);
  rightBack.run(RELEASE);
  leftFront.run(RELEASE);
  leftBack.run(RELEASE);
  // continue;
}

void moveForward() {
  rightFront.run(FORWARD);
  rightBack.run(FORWARD);
  leftFront.run(BACKWARD);
  leftBack.run(BACKWARD);
  // continue;
}

void moveBackward() {
  rightFront.run(BACKWARD);
  rightBack.run(BACKWARD);
  leftFront.run(FORWARD);
  leftBack.run(FORWARD);
  // continue;
}

void moveRight() {

  resetSpeed(motorTurnSpeed);
  rightFront.run(BACKWARD);
  rightBack.run(BACKWARD);
  leftFront.run(BACKWARD);
  leftBack.run(BACKWARD);
  delay(timeForTurnStationary);
  stopMoving();
  resetSpeed();
  // continue;
}

void moveLeft() {
  resetSpeed(motorTurnSpeed);
  rightFront.run(FORWARD);
  rightBack.run(FORWARD);
  leftFront.run(FORWARD);
  leftBack.run(FORWARD);
  delay(timeForTurnStationary);
  stopMoving();
  resetSpeed();
  // continue;
}

void moveRightWhileMoving() {
  // resetSpeed(motorFast);
  // rightFront.setSpeed(motorSlow);
  // rightBack.setSpeed(motorSlow);
  // // moveForward();
  // delay(timeForTurnMoving);

  //set speed back to normal and continue moving after turn
  // rightFront.setSpeed(motorSpeedDefault);
  // rightBack.setSpeed(motorSpeedDefault);
  // resetSpeed();
  // moveForward()
  resetSpeed(motorFast);
  rightFront.setSpeed(motorSlow);
  rightBack.setSpeed(motorSlow);
  rightFront.run(BACKWARD);
  rightBack.run(BACKWARD);
  leftFront.run(BACKWARD);
  leftBack.run(BACKWARD);
  delay(timeForTurnMoving);
  moveForward();
  resetSpeed();
}

void moveLeftWhileMoving() {
  // resetSpeed(motorFast);
  // leftFront.setSpeed(motorSlow);
  // leftBack.setSpeed(motorSlow);
  // // moveForward();
  // delay(timeForTurnMoving);

  // //set speed back to normal and continue moving after turn
  // // leftFront.setSpeed(motorSpeedDefault);
  // // leftBack.setSpeed(motorSpeedDefault);
  // resetSpeed();
  // // moveForward()


  resetSpeed(motorFast);
  leftFront.setSpeed(motorSlow);
  leftBack.setSpeed(motorSlow);
  rightFront.run(FORWARD);
  rightBack.run(FORWARD);
  leftFront.run(FORWARD);
  leftBack.run(FORWARD);
  delay(timeForTurnMoving);
  moveForward();
  resetSpeed();
}





void setup(){
  // put your setup code here, to run once:
  Serial.begin(9600);//Initialize communications to the serial monitor in the Arduino IDE
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  // serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  Serial.println("Started");//Tell the serial monitor that the sketch has started.


  resetSpeed();


}







void loop(){
  //This will prevent bufferoverrun errors

  

  byte byte_count=serial_connection.available();//This gets the number of bytes that were sent by the python script

  if(byte_count) { //If there are any bytes then deal with them
    Serial.println("Incoming Data");//Signal to the monitor that something is happening
    int first_bytes=byte_count;//initialize the number of bytes that we might handle. 
    int remaining_bytes=0;//Initialize the bytes that we may have to burn off to prevent a buffer overrun

    if(first_bytes>=BUFFER_SIZE-1) {//If the incoming byte count is more than our buffer...
      remaining_bytes=byte_count-(BUFFER_SIZE-1);//Reduce the bytes that we plan on handleing to below the buffer size
    }

    for(i=0;i<first_bytes;i++) {//Handle the number of incoming bytes
      inChar=serial_connection.read();//Read one byte
      inData[i]=inChar;//Put it into a character string(array)
    }

    inData[i]='\0';
    // moveForward();
    // delay(1000);
    // stopMoving();//This ends the character array with a null character. This signals the end of a string


//Start writing conditions here

    // if(String(inData)=="BOOP 2")//This could be any motor start string we choose from the python script
    // {
    //   Serial.println("********* Start Motor *********");
    // }
    // else if(String(inData)=="BOOP 4")//Again this is an arbitrary choice. It would probably be something like: MOTOR_STOP
    // {
    //   Serial.println("********* STOP Motor *********");
    // }

    if(String(inData) == "Forward") {
      moveForward();
      text = "Moving Forward";
      carMoving = true;
    }

    if(String(inData) == "Backward") {
      moveBackward();
      text = "Moving Backward";
      carMoving = true;
    }

    if(String(inData) == "Right") {
      text = "Moving Right";
      if(carMoving) {
        moveRightWhileMoving();
      }
      else {
        moveRight();
      }
    }

    if(String(inData) == "Left") {
      text = "Moving Left";
      if(carMoving) {
        moveLeftWhileMoving();
      }
      else {
        moveLeft();
      }
    }

    if(String(inData) == "Stop") {
      stopMoving();
      text = "Stopped Moving";
      carMoving = false;
    }

    if(String(inData) == "Reset") {
      resetSpeed();
      text = "Speed reset";
    }

// Stop conditions



    for(i=0;i<remaining_bytes;i++) {//This burns off any remaining bytes that the buffer can't handle.
      inChar=serial_connection.read();
    }

    Serial.println(inData);//Print to the monitor what was detected
    serial_connection.println(text);//Then send an incrmented string back to the python script
    // count++;//Increment the line counter
  }

  delay(100);//Pause for a moment 
}