/*******************************************************************************
* Modulacao do tom de uma musica. A nota é multiplicada por um coeficiente angular de reta para o ajuste do tom:
* 
* modulacao = ( (2 - 0.5) / 1023) * leitura + 0.5 –––> coef angular é o ajuste do tom
* 
* pot = 0 ––––––> uma oitava abaixo
* pot = 1023 –––> uma oitava acima
********************************************************************************/

const int pino_potenciometro = A0; // pino onde o potenciometro está conectado
int leitura = 0; // variável para armazenar o valor lido pelo ADC
const int buzzer = 2;
const float do1  = 261.63;
const float re  = 293.66;
const float mi  = 329.63;
const float fa  = 349.23;
const float sol = 391.99;
const float la  = 440.00;
const float si  = 493.88;
const float do2 = 523.26;

void setup() {
  // Inicia e configura a Serial
  Serial.begin(9600); // 9600 bps

  // configura o pino com potenciometro como entrada
  pinMode(pino_potenciometro, INPUT); // pino A0
  pinMode(buzzer, OUTPUT);
}

void loop() {
  leitura = analogRead (pino_potenciometro);
  Serial.println(leitura);
  tone(buzzer, do1*(leitura*1.5/1023+0.5));
/*  delay(250);

  leitura = analogRead (pino_potenciometro);
  Serial.print(leitura);
  tone(buzzer, re*(leitura*1.5/1023+0.5));
  delay(250);
  
  leitura = analogRead (pino_potenciometro);
  Serial.print(leitura);
  tone(buzzer, mi*(leitura*1.5/1023+0.5));
  delay(250);

  leitura = analogRead (pino_potenciometro);
  Serial.print(leitura);
  tone(buzzer, fa*(leitura*1.5/1023+0.5));
  delay(250);
  
  leitura = analogRead (pino_potenciometro);
  Serial.print(leitura);
  tone(buzzer, sol*(leitura*1.5/1023+0.5));
  delay(250);

  leitura = analogRead (pino_potenciometro);
  Serial.print(leitura);
  tone(buzzer, la*(leitura*1.5/1023+0.5));
  delay(250);
  
  leitura = analogRead (pino_potenciometro);
  Serial.print(leitura);
  tone(buzzer, si*(leitura*1.5/1023+0.5));
  delay(250);

  leitura = analogRead (pino_potenciometro);
  Serial.print(leitura);
  tone(buzzer, do2*(leitura*1.5/1023+0.5));
  delay(250);


    / Frequências
   * Dó  - 261,63Hz
   * Ré  - 293,66Hz
   * Mi  - 329,63Hz
   * Fá  - 349,23Hz
   * Sol - 391,99Hz
   * Lá  - 440,00Hz
   * Si  - 493,88Hz
   */
}

