/* Pecas: 1 buzzer, 2 chaves momentaneas, 2 LEDs,
 *        2 resistores 300 ohms, 2 resistores 10k ohm.
 */


const int pino_botao_amarelo = 7  ;  // botao amarelo === pino 7
const int pino_botao_verde   = 8  ;  // botao verde ===== pino 8

const int pino_led_amarelo   = 11 ; // led amarelo ====== pino 11
const int pino_led_verde     = 12 ; // led verde ======== pino 12
const int pino_buzzer        = 2  ; // buzzer =========== pino 2

int estado_botao_amarelo     = 0  ;  // botao amarelo === desligado
int estado_botao_verde       = 0  ;  // botao verde ===== desligado


void setup() {
  pinMode (pino_botao_amarelo, INPUT) ; // botao amarelo === input
  pinMode (pino_botao_verde, INPUT)   ; // botao verde ===== input
  pinMode (pino_led_amarelo, OUTPUT)  ; // led amarelo ===== output
  pinMode (pino_led_verde, OUTPUT)    ; // led verde ======= output
  pinMode (pino_buzzer, OUTPUT)       ; // buzzer ========== output

}


void loop() {
  estado_botao_amarelo = digitalRead (pino_botao_amarelo) ;
  estado_botao_verde = digitalRead (pino_botao_verde)     ;

  // Dois botoes SOLTOS
  if (!estado_botao_amarelo && !estado_botao_verde){
    digitalWrite (pino_led_amarelo, LOW) ;
    digitalWrite (pino_led_verde, LOW)   ;
    noTone (pino_buzzer)                 ;
                                                   }
  // Botao amarelo LIGADO
  if (estado_botao_amarelo && !estado_botao_verde){
    digitalWrite (pino_led_amarelo, HIGH) ;
    digitalWrite (pino_led_verde, LOW)    ;
    tone (pino_buzzer, 261.63)            ; // Do
                                                  }

  // Botao verde LIGADO
  if (!estado_botao_amarelo && estado_botao_verde){
    digitalWrite (pino_led_amarelo, LOW) ;
    digitalWrite (pino_led_verde, HIGH)  ;
    tone (pino_buzzer, 391.99)           ;  // Sol
                                                  }

  // Dois botoes LIGADOS
  if (estado_botao_amarelo && estado_botao_verde){
  digitalWrite (pino_led_amarelo, HIGH) ;
  digitalWrite (pino_led_verde, HIGH)    ;
  tone (pino_buzzer, 329.63)            ;  // Re
                                                 }

  /* Frequências
   * Dó  - 261,63Hz
   * Ré  - 293,66Hz
   * Mi  - 329,63Hz
   * Fá  - 349,23Hz
   * Sol - 391,99Hz
   * Lá  - 440,00Hz
   * Si  - 493,88Hz
   */

}
