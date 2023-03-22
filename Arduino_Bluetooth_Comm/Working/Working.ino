#include <AFMotor.h>
// #include <ctime>
int frontRight = 4;
int frontLeft = 1;
int backRight = 3;
int backLeft = 2;
AF_DCMotor rightFront(frontRight);
AF_DCMotor rightBack(backRight);
AF_DCMotor leftFront(frontLeft);
AF_DCMotor leftBack(backLeft);

int timeForTurnStationary = 1000;
int timeForTurnMoving = 1000;

int motorSpeedDefault = 100;
int differenceInSpeed = 50;

int  timeInitial = millis();
bool moveFlag = false;
int switcher = 1;


void moveForward() {
  rightFront.run(FORWARD);
  rightBack.run(FORWARD);
  leftFront.run(BACKWARD);
  leftBack.run(BACKWARD);
}

void moveBackward() {
  rightFront.run(BACKWARD);
  rightBack.run(BACKWARD);
  leftFront.run(FORWARD);
  leftBack.run(FORWARD);
}

void moveRight() {
  rightFront.run(BACKWARD);
  rightBack.run(BACKWARD);
  leftFront.run(BACKWARD);
  leftBack.run(BACKWARD);
  delay(timeForTurnStationary);
}

void moveLeft() {
  rightFront.run(FORWARD);
  rightBack.run(FORWARD);
  leftFront.run(FORWARD);
  leftBack.run(FORWARD);
  delay(timeForTurnStationary);
}

void moveRightWhileMoving() {
  rightFront.setSpeed(motorSpeedDefault - differenceInSpeed);
  rightBack.setSpeed(motorSpeedDefault - differenceInSpeed);
  moveForward();
  delay(timeForTurnMoving);
  rightFront.setSpeed(motorSpeedDefault);
  rightBack.setSpeed(motorSpeedDefault);
}

void moveLeftWhileMoving() {
  leftFront.setSpeed(motorSpeedDefault - differenceInSpeed);
  leftBack.setSpeed(motorSpeedDefault - differenceInSpeed);
  moveForward();
  delay(timeForTurnMoving);
  leftFront.setSpeed(motorSpeedDefault);
  leftBack.setSpeed(motorSpeedDefault);
}

void stopMoving() {
  rightFront.run(RELEASE);
  rightBack.run(RELEASE);
  leftFront.run(RELEASE);
  leftBack.run(RELEASE);
}








void setup() {
  // put your setup code here, to run once:
  rightFront.setSpeed(motorSpeedDefault);
  rightBack.setSpeed(motorSpeedDefault);
  leftBack.setSpeed(motorSpeedDefault);
  leftFront.setSpeed(motorSpeedDefault);


  // moveForward();
  // delay(3000);
  // stopMoving();
  // delay(2000);
  // moveBackward();
  // delay(3000);
  // stopMoving();
  // delay(1000);
  // moveRight();
  // delay(1000);
  // moveLeft();
  // delay(1000);
  // moveForward();
  // delay(2000);
  // moveRightWhileMoving();
  // delay(1000);
  // moveLeftWhileMoving();
  // delay(2000);
  // stopMoving();
  // delay(1000);

  // int  timeInitial = millis();
  // bool moveFlag = false;
}


void loop() {
  // put your main code here, to run repeatedly:
  

  // moveLeft();
  // delay(2000);
  // moveRight();
  // delay(2000);
  // int  timeCurrent = millis();
  // int difference = 3001 * switcher;
  // if (timeCurrent > difference) {
  //   if (difference%2 == 0) {
  //     rightFront.run(FORWARD);
  //   }
  //   else {
  //     rightFront.run(RELEASE);
  //   }
  //   switcher++;
  // moveForward();
    
  // }

  // // if(timeCurrent > timeInitial+3) {
  // //   timeInitial = timeCurrent;
  // //   if(moveFlag) {
  // //     rightFront.run(FORWARD);
  // //   }
  // //   else {
  // //     rightFront.run(RELEASE);
  // //   }
  // // }1
    // leftFront.setSpeed(100);
    // leftFront.run(FORWARD);
    moveLeft();




}
