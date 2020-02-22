const char ldr = A0;
const char led = 11;

int estldr;
unsigned char pwm = 0;

void setup() {
  Serial.begin(9600);
  pinMode(led , OUTPUT);
}

void loop() {
  estldr = analogRead(ldr);
  if(estldr < 300){ if(pwm < 250){ pwm++; }}
  else if(estldr >= 300){if(pwm > 0){ pwm--; }}
  analogWrite(led , pwm);
  
  Serial.print("estldr: ");
  Serial.print(estldr);
  Serial.println();
  Serial.print("pwm: ");
  Serial.print(pwm);
  Serial.println();
  Serial.println();
  delay(10);
}
