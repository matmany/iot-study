#include "max6675.h"
 
const int ktcSO = 8; 
const int ktcCS = 9; 
const int ktcCLK = 7;
const int ldr = A5;
 
MAX6675 ktc(ktcCLK, ktcCS, ktcSO);

double convertToLux(int ldrReading){
  double Vout=ldrReading*0.0048828125;
  int lux=(2500/Vout-500)/10;
  return lux;
 }

void setup(){
  Serial.begin(9600);
  pinMode(ldr, INPUT);
  delay(500);
}
 
void loop(){
  if(Serial.available()){
    switch(Serial.read()){
      case 'C':
        Serial.print(ktc.readCelsius());
        break;
      case 'L':
        Serial.print(convertToLux(analogRead(ldr)));
        break;
      }
      delay(500);
   }
}
