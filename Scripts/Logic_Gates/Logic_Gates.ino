const byte pinA = 2;
const byte pinB = 3;
const byte OR = 4;
const byte AND = 5;
const byte NOR = 6;
const byte NAND = 7;
bool A, B;
byte i=0;

void funcOR(bool A, bool B){
  bool Y;
  if(A || B){
    Y = 1;
  }
  else{
    Y = 0;
  }
  digitalWrite(OR, Y);
}

void funcAND(bool A, bool B){
  bool Y;
  if(A && B){
    Y = 1;
  }
  else{
    Y = 0;
  }
  digitalWrite(AND, Y);
}

void funcNOR(bool A, bool B){
  bool Y;
  if(!A || !B){
    Y = 1;
  }
  else{
    Y = 0;
  }
  digitalWrite(NOR, Y);
}

void funcNAND(bool A, bool B){
  bool Y;
  if(!A & !B){
    Y = 1;
  }
  else{
    Y = 0;
  }
  digitalWrite(NAND, Y);
}

void setup() {
  Serial.begin(9600);
  pinMode(pinA, INPUT);
  pinMode(pinB, INPUT);
  pinMode(OR, OUTPUT);
  pinMode(AND, OUTPUT);
  pinMode(NOR, OUTPUT);
  pinMode(NAND, OUTPUT);
  for(i=4 ; i<8 ; i++){
    digitalWrite(i, LOW);
  }
}

void loop() {
  A = digitalRead(pinA);
  B = digitalRead(pinB);
  funcOR(A, B);
  funcAND(A, B);
  funcNOR(A, B);
  funcNAND(A, B);
}
