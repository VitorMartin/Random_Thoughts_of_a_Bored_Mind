const int pino_res = A0;
int leitura_res = 0;
int corrente = 0;
const int r = 2;
const int g = 4;
const int y = 7;
const int w = 8;
const int wait = 100;

void setup() {
  Serial.begin(9600);
  pinMode(pino_res, INPUT);
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(y, OUTPUT);
  pinMode(w, OUTPUT);

}

void loop() {
  leitura_res = analogRead(pino_res);
  Serial.println(leitura_res);
  
  digitalWrite(r, HIGH);
  delay(wait);
  digitalWrite(g, HIGH);
  delay(wait);
  digitalWrite(y, HIGH);
  delay(wait);
  digitalWrite(w, HIGH);
  delay(wait);

  digitalWrite(r, LOW);
  delay(wait);
  digitalWrite(g, LOW);
  delay(wait);
  digitalWrite(y, LOW);
  delay(wait);
  digitalWrite(w, LOW);
  delay(wait);


}
