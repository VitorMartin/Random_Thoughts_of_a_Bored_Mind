//Programa : Teste Arduino Mini
//Autor : Arduino e Cia
 
int portaled = 7;
 
void setup()
{
  pinMode(portaled, OUTPUT);
}
 
void loop()
{
  digitalWrite(portaled, HIGH);
  delay(100);
  digitalWrite(portaled, LOW);
  delay(100);
}
