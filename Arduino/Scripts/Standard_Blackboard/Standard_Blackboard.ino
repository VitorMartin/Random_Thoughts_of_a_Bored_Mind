byte pwm9, pwm10, pwm11;

byte pwm(float v){
  v = v/5*255;
  return v;
}

void setup() {
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);

  digitalWrite(8, LOW);
  analogWrite(9, pwm(1.9));
  analogWrite(10, pwm(2.7));
  analogWrite(11, pwm(4.1));
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);
}

void loop(){
  
}
