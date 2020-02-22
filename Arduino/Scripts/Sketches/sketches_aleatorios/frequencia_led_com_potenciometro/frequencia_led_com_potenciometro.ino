const int pino_pot = A0;
const int pino_led = 11;
float leitura_pot = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pino_pot, INPUT);
  pinMode(pino_led, OUTPUT);

}

void loop() {
  leitura_pot = analogRead(pino_pot);
  if(leitura_pot<1){
    leitura_pot = 1;
    }

  digitalWrite(pino_led, HIGH);
  delay(1/leitura_pot);

  digitalWrite(pino_led, LOW);
  delay(1/leitura_pot);

  Serial.print(leitura_pot);
  Serial.print("\t");
  Serial.print(1/leitura_pot);
  Serial.println();

}
