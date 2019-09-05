int pin = 3 ;
volatile int pulses;
unsigned long time1=0;
void setup() 
{
  Serial.begin(9600);
  pinMode(pin,INPUT);

  attachInterrupt(digitalPinToInterrupt(pin),interrupt,FALLING);
  time1=millis();
}

void loop() 
{
  if (digitalRead( pin) == HIGH)
   {
  if(   millis()-time1>=1150)
  {
  switch (pulses) {
       case 1 :
     Serial.println(" 0.5 pound ");
        break;
        case 2 :
    Serial.println(" 1 pound ");
        break;
       default:
        break;
}
    pulses=0;
    time1=millis();
  }}
}
void interrupt()
{
  pulses++;
}
