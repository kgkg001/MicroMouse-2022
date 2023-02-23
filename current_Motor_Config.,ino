//EXAMPLE CODE TO MAKE THE MICROMOUSE OF 2022/23 GO FORWARD, TURN RIGHT AND LEFT
//OPTIMIZATIONS CAN BE DONE, BUT THIS IS THE MOST BASIC FORM OF TURNING
//WRITTEN BY OWEN FARRELL

// Include the Arduino Stepper Library
#include <Stepper.h>

// Number of steps per output rotation
const int stepsPerRevolution = 200;

// Create Instance of Stepper library
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);


void setup()
{
  // set the speed at 60 rpm:
  myStepper.setSpeed(60);
  // initialize the serial port:
  Serial.begin(9600);
  // initialize the output pins. This code works by enabling and disabling the motor shields
  // for our code 7 is left and 6 is right
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop() 
{
  
  // FORWARD
  // both motors on  
  digitalWrite(7, HIGH);// < left motor on
  digitalWrite(6, HIGH);// < right motor on
  // \/ this function takes a int value, and is simply the number of steps output by the stepper. can be negative, means reverse
  myStepper.step(stepsPerRevolution);

  // LEFT
  // left motor off
  digitalWrite(7, LOW);
  digitalWrite(6, HIGH);  
  myStepper.step(stepsPerRevolution); 

  //RIGHT
  // right motor off
  digitalWrite(7, HIGH);
  digitalWrite(6, LOw);
  myStepper.step(stepsPerRevolution);
}