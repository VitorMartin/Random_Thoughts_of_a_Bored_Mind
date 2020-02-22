/*******************************************************************************
* RoboCore Arduino Pocket Kit - Projeto Iluminação Automatizada
* Acender o LED gradativamente quando a luminosidade do ambiente estiver abaixo
* de um limite.
*******************************************************************************/

const int pino_ldr = A0; // pino onde o LDR está conectado
const int pino_led = 11; // pino onde o LED está conectado
int leitura = 0; // variável para armazenar o valor lido pelo ADC
int pwm = 0; // variável para armazenar o valor da razão cíclica (duty cycle) 

void setup() {
  Serial.begin(9600); 
  pinMode(pino_ldr, INPUT); // configura o pino com LDR como entrada
  pinMode(pino_led, OUTPUT); // configura o pino com o LED como saída
}

void loop() {
  // le o valor de tensão no pino do potenciômetro
  leitura = analogRead(pino_ldr);
  
  if (leitura < 700) { // se a leitura for menor que 700 (pouca luminosidade)
    pwm++; // pwm = pwm + 1; // incrementa a variável pwm
  }
  else { // senão, apaga o LED
    pwm = 0; // apaga o LED
  }
  
  if (pwm > 255) { // se o valor for maior que o máximo (255)
    pwm = 255; // seta o valor para o máximo (255)
  }
  
  // atualiza a razão cíclica do pino 11, variando a intensidade do led
  analogWrite(pino_led, pwm);

  Serial.print("Leitura: ");
  Serial.print(leitura);
  Serial.print("\t");
  Serial.print("PWM: ");
  Serial.print(pwm);
  Serial.println();
  
  delay(30); // aguarda 100ms para uma nova leitura
  
}
