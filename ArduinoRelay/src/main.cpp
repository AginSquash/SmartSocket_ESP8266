#include <Arduino.h>
#include <SPI.h>

#define RELAY A4


void setup() {
  Serial.begin(115200);
  pinMode(RELAY, OUTPUT);
}

void loop() {
  
  String command = Serial.readStringUntil('\n');
  command.trim();

  if (command=="relay=1")
  {
    digitalWrite(RELAY, HIGH);
    Serial.println("relay=1");
  }

  if (command=="relay=0")
  {
    digitalWrite(RELAY, LOW);
    Serial.println("relay=0");
  }

}