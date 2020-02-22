const int pinos_leds[] = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
const int pino_termistor = A0; // pino onde o termistor está conectado
const int pino_buzzer = 2; // pino onde o buzzer está conectado
const float resistor_serie = 10000.0; // valor do resistor em serie com o termistor
const float resistencia_nominal = 10000.0; // resistencia nominal do termistor
const float temperatura_nominal = 25.0; // temperatura para resistência nominal
const float coeficiente_beta = 3950.0; // coeficiente beta do sensor (datasheet)
int leitura = 0; // variável para armazenar o valor lido pelo ADC
float resistencia = 0.0; // variável para armazenar a resistência
float temperatura = 0.0; // variável para armazenar a temperatura


void setup() {
  for(int x = 0; x < 10; x++){
    pinMode(pinos_leds[x], OUTPUT);
    }
}

void loop() {
  digitalWrite(3, HIGH);
  delay(300);
  digitalWrite(4, HIGH);
  delay(300);
  digitalWrite(5, HIGH);
  delay(300);
  digitalWrite(6, HIGH);
  delay(300);
  digitalWrite(7, HIGH);
  delay(300);
  digitalWrite(8, HIGH);
  delay(300);
  digitalWrite(9, HIGH);
  delay(300);
  digitalWrite(10, HIGH);
  delay(300);
  digitalWrite(11, HIGH);
  delay(300);
  digitalWrite(12, HIGH);
  delay(300);
    
//  for(int x = 3; x < 13; x++){
//  digitalWrite(x, HIGH);
//  delay(100);
//  }
//  for(int x = 0; x < 10; x++){
//  digitalWrite(pinos_leds[x], LOW);
//  delay(300);
//  }
}
