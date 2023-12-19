#include <ESP32_Servo.h>

Servo myservo;  // create servo object to control a servo
                // 16 servo objects can be created on the ESP32

int pos = 0;    // variable to store the servo position
// Recommended PWM GPIO pins on the ESP32 include 2,4,12-19,21-23,25-27,32-33 
int servoPin = 18;

void setup() {
  myservo.attach(servoPin);   // attaches the servo on pin 18 to the servo object
                              // using default min/max of 1000us and 2000us
                              // different servos may require different min/max settings
                              // for an accurate 0 to 180 sweep
}

void loop() {
  delay(500);
  myservo.write(120);
  // delay(500);
  // myservo.write(45);
  // delay(500);
  // myservo.write(90);
  // delay(500);
  // myservo.write(135);
  delay(1000);
  // myservo.write(0);
}

void open() {
  myservo.write(0);
  delay(15);
}

void off() {
  myservo.write(180);
  delay(15);
}

