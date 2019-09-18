
const int ledPin = 13; 
int serial ;      // a variable to read incoming serial 

int pin = 2 ;
volatile int pulses;
float counter = 0.0;
unsigned long time1 = 0;

char x ;

 long start_time , end_time ,i=1;
 int average ;

 
void setup() {
  
  Serial.begin(9600);

  pinMode(pin, INPUT);
  attachInterrupt(digitalPinToInterrupt(pin), interrupt, FALLING);
  time1 = millis();
  
  pinMode(ledPin, OUTPUT);
}

void loop() {
 if (Serial.available()){

   serial = Serial.read();
 }

  while(serial > '0' ){
if (digitalRead( pin) == HIGH)
  {
    if (   millis() - time1 >= 1150)
    {
      switch (pulses) {
        case 1 :
          // Serial.println(" 0.5 pound ");
          counter = counter + 0.5;
          break;
        case 2 :
          //Serial.println(" 1 pound ");
          counter = counter + 1.0;

          break;
        default:
          break;
      }
      if (pulses > 2) {
      //  Serial.println ("ERROR");
      }
      pulses = 0;
      time1 = millis();
    }
  }
 // Serial.println ( counter);





   // start_time = millis();
   
   if (counter == 10 && serial == '9') {
      counter = 0;
      x = 'n' ;
     Serial.print(x);
     serial = '0' ;
   
     break;
    }
     if (counter == 7 && serial == '7') {
      counter = 0;
      x = 's' ;
     Serial.print(x);
     serial = '0' ;
   
     break;
    }
     if (counter == 5 && serial == '5') {

      counter = 0;
      x = 'f' ;
     Serial.print(x);
     serial = '0' ;
   
     break;
     }
     
     if (counter == 3 && serial == '3' ) {
     
      counter = 0;
      x = 't' ;
     Serial.print(x);
     serial = '0' ;
   
     break;
    
    }

  }
  //Serial.println("end loop");
  
/*
counter = 0;

end_time = millis();

average = end_time - start_time ;
i++;
  
/*
 * 
 *  read type of ticket 3-5-7-10
 * 
  if (Serial.available() ) {
    // read the oldest byte in the serial buffer:
    serial = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (serial == '3') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (serial == '9') {
      digitalWrite(ledPin, LOW);
    }
  }
*/



}


//////////////////////////////////////////////////////////////

void interrupt()
{
  pulses++;
}








