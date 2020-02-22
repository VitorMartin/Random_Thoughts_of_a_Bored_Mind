const int pino_buzzer = 2;

void setup() {
  pinMode (pino_buzzer, OUTPUT);

}

void loop() {
  tone (pino_buzzer, 261.63);

  tone (pino_buzzer, 391.99);

  tone (pino_buzzer, 329.63);


}
