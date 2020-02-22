const char seg[] = {2, 3, 4, 5, 6, 7, 8, 9}; // Arduino pins from A to G, then DOT
//                  A  B  C  D  E  F  G  DOT
//                  0  1  2  3  4  5  6  7
const char A = 0;
const char B = 1;
const char C = 2;
const char D = 3;
const char E = 4;
const char F = 5;
const char G = 6;
const char DOT = 7;
char n;
bool decimal;


void displayNum(char n, bool decimal){
  Serial.print("Character: ");
  Serial.print(n);
  Serial.print("\t");
  Serial.print("Decimal: ");
  Serial.println(decimal);
  if(decimal){
    digitalWrite(seg[DOT], 1);
  }
  else{
    digitalWrite(seg[DOT], 0);
  }
  if(n == ' '){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 0);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 0);
    digitalWrite(seg[F]  , 0);
    digitalWrite(seg[G]  , 0);
  }
  else if(n == 0){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 0);
  }
  else if(n == 1){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 0);
    digitalWrite(seg[F]  , 0);
    digitalWrite(seg[G]  , 0);
  }
  else if(n == 2){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 0);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 0);
    digitalWrite(seg[G]  , 1);
  }
  else if(n == 3){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 0);
    digitalWrite(seg[F]  , 0);
    digitalWrite(seg[G]  , 1);
  }
  else if(n == 4){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 0);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);

  }
  else if(n == 5){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 0);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
  else if(n == 6){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
  else if(n == 7){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 0);
    digitalWrite(seg[F]  , 0);
    digitalWrite(seg[G]  , 0);
  }
  else if(n == 8){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
  else if(n == 9){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 0);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
  else if((n == 'a') || (n == 'A')){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
  else if((n == 'b') || (n == 'B')){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
    else if(n == 'c'){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 0);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 0);
    digitalWrite(seg[G]  , 1);
  }
    else if(n == 'C'){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 0);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 0);
  }
    else if((n == 'd') || (n == 'D')){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 0);
    digitalWrite(seg[G]  , 1);
  }
    else if((n == 'e') || (n == 'E')){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 0);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
    else if((n == 'f') || (n == 'F')){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 0);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
    else if((n == 'h') || (n == 'H')){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
    else if((n == 'j') || (n == 'J')){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 0);
    digitalWrite(seg[G]  , 0);
  }
    else if((n == 'l') || (n == 'L')){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 0);
    digitalWrite(seg[C]  , 0);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 0);
  }
    else if((n == 'p') || (n == 'P')){
    digitalWrite(seg[A]  , 1);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 0);
    digitalWrite(seg[D]  , 0);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 1);
  }
    else if((n == 'u') || (n == 'U')){
    digitalWrite(seg[A]  , 0);
    digitalWrite(seg[B]  , 1);
    digitalWrite(seg[C]  , 1);
    digitalWrite(seg[D]  , 1);
    digitalWrite(seg[E]  , 1);
    digitalWrite(seg[F]  , 1);
    digitalWrite(seg[G]  , 0);
  }
  else{'character cannot be displayed';}
}


void displayBar(bool a, bool b, bool c, bool d, bool e, bool f, bool g, bool decimal){
//  for(char i = 0; i < 8; i++){
//    digitalWrite(seg[i], inp[i]);
  
  digitalWrite(seg     , 0);
  digitalWrite(seg[A]  , a);
  digitalWrite(seg[B]  , b);
  digitalWrite(seg[C]  , c);
  digitalWrite(seg[D]  , d);
  digitalWrite(seg[E]  , e);
  digitalWrite(seg[F]  , f);
  digitalWrite(seg[G]  , g);
  digitalWrite(seg[DOT], decimal);
}

void setup() {
  Serial.begin(9600);
  pinMode(seg, OUTPUT);
}


void loop() {  
  
}
