#include <stdio.h>

// pinos onde cada um dos bits estão conectados:
const int out_a = A0;
const int out_b = A1;
const int out_c = A2;
const int out_d = A3;
const int ba = 10;
const int bb = 11;
const int bc = 12;
const int bd = 13;
bool a, b, c, d;

void setup() {
  Serial.begin(9600);
  pinMode(out_a, OUTPUT);
  pinMode(out_b, OUTPUT);
  pinMode(out_c, OUTPUT);
  pinMode(out_d, OUTPUT);
  pinMode(ba, INPUT);
  pinMode(bb, INPUT);
  pinMode(bc, INPUT);
  pinMode(bd, INPUT);
}

void loop() {
   a = digitalRead(ba);
   b = digitalRead(bb);
   c = digitalRead(bc);
   d = digitalRead(bd);

   if(d&&c || d&&b){
      
   }
   digitalWrite(out_a, a);
   digitalWrite(out_b, b);
   digitalWrite(out_c, c);
   digitalWrite(out_d, d);

   Serial.print("d = ");
   Serial.print(d);
   Serial.print("\t");
   Serial.print("c = ");
   Serial.print(c);
   Serial.print("\t");
   Serial.print("b = ");
   Serial.print(b);
   Serial.print("\t");
   Serial.print("a = ");
   Serial.print(a);
   Serial.print("\t");
   Serial.println();
}
