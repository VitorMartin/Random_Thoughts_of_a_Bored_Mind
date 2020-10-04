#include <IRremote.h>

const char infra = 4;
const char control = 13;

IRrecv irrecv(infra);

decode_results results;

void setup()
{
  digitalWrite(control, LOW);
  pinMode(control, OUTPUT);
  Serial.begin(9600);
  Serial.println("Enabling IRin");
  irrecv.enableIRIn(); // Start the receiver
  Serial.println("IRin Enabled");
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    if(results.value == 0x10031 || results.value == 0x31){
      digitalWrite(control, HIGH); // Toggle
      delay(500);
      digitalWrite(control, LOW);
      delay(1000);
    }
    irrecv.resume(); // Receive the next value
  }
  delay(100);
}
