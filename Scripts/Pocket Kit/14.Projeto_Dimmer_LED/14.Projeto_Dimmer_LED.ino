/*******************************************************************************
* RoboCore Arduino Pocket Kit - Projeto Dimmer LED
* Usar um potenciômetro para controlar a intensidade luminosa de um LED.
*******************************************************************************/

const int pino_potenciometro = A0; // pino onde o pontenciômetro está conectado
const int pino_led = 11; // pino onde o LED está conectado
int leitura = 0; // variável para armazenar o valor lido pelo ADC
int pwm = 0; // variável para armazenar o valor da razão cíclica (duty cycle) 

void setup() {
  Serial.begin(9600);
  pinMode(pino_potenciometro, INPUT); // configura o pino com potenciômetro como entrada
  pinMode(pino_led, OUTPUT); // configura o pino com o LED como saída
}

void loop() {
  // le o valor de tensão no pino do potenciômetro
  leitura = analogRead(pino_potenciometro);
  
  // converte o valor do potenciômetro, de 0 a 1023, em um valor de 0 a 255
  pwm = map(leitura, 0, 1023, 0, 255); 
  
  // atualiza a razão cíclica do pino 11, variando a intensidade do LED
  analogWrite(pino_led, pwm);

  Serial.print("Leitura: ");
  Serial.print(leitura);
  Serial.print("\t");

  Serial.print("PWM: ");
  Serial.print(pwm);
  Serial.print("\t");

  Serial.println();
}
