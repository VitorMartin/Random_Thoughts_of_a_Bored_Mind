const int ledest = 10;
const int pot_pin = A5;
int pot;

void setup() {
  Serial.begin(9600);
  pinMode(ledest, OUTPUT);
  pinMode(pot_pin, INPUT);
}

void loop() {
  pot = map(analogRead(pot_pin), 0, 1023, 0, 255);
  analogWrite(ledest, pot);
  Serial.println(pot);
}
