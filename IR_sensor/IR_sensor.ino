#include <IRremote.h>

const int recv_pin = 9;      // Pin connected to the IR sensor output
const int led_pin = 13;      // Pin connected to the LED

void setup() {
  Serial.begin(9600);        // Start serial communication for debugging
  //irrecv.enableIRIn();       // Start the IR receiver
  pinMode(recv_pin,INPUT);
  pinMode(led_pin, OUTPUT);  // Set the LED pin as an output
}

void loop() {
  int sensor_value = digitalRead(recv_pin);
  if (sensor_value == LOW) { 
    digitalWrite(led_pin, HIGH);
    Serial.println("1");
    delay(2000);
  }
  else{
    digitalWrite(led_pin, LOW);
    Serial.println("0");
    delay(1000);
  }
  
}