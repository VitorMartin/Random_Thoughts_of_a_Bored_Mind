#include <IRremote.h>

const char infra = 7;
const char rele = 8;

IRrecv irrecv(infra);

decode_results results;

void setup()
{
  Serial.begin(9600);
  pinMode(rele, OUTPUT);
  digitalWrite(rele, LOW);
  Serial.println("Enabling IRin");
  irrecv.enableIRIn(); // Start the receiver
  Serial.println("Enabled IRin");
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    if(results.value == 0x10037 || results.value == 0x37){
      if(digitalRead(rele) == LOW){
        digitalWrite(rele, HIGH);
        delay(2000);
      }
      else{
        digitalWrite(rele, LOW);
        delay(2000);
      }
    }
    irrecv.resume(); // Receive the next value
  }
  delay(100);
}
