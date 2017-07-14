// CIRC10: TEMPERATURE 
// Works with the Metro AND the Metro Express!!


/* Metro/Metro Express Select
   Set which board you own to true
*/ 
// I have a Metro
#define Metro false
// I have a Metro EXPRESS 
#define MetroExpress false

//TMP36 Pin Variables
int temperaturePin = 0; //the analog pin the TMP36's Vout (sense) pin is connected to
                        //the resolution is 10 mV / degree centigrade 
                        //(500 mV offset) to make negative temperatures an option

/*
 * setup() - this function runs once when you turn your Arduino on
 * We initialize the serial connection with the computer
 */
void setup()
{
  // Start the Serial connection
  Serial.begin(9600);  
}
 
void loop()                     // run over and over again
{
 float temperature = 0;
 /* Board Select */
 if(Metro == true) {
  temperature = getVoltage5V(temperaturePin);
 }
 else if(MetroExpress == true) {
  temperature = getVoltage3V(temperature);
 }
 else if((Metro == false and MetroExpress == false) or (Metro == true and MetroExpress == true)){
   Serial.println("error, select a board");
 }
 
 // Convert to degrees C
 temperature = (temperature - .5) * 100;          
                                                  
 Serial.println(temperature);                     
 delay(1000);                                     
}

// Metro, 5V
float getVoltage5V(int pin){
 // 5V/1023
 return (analogRead(pin) * .004882814);                         
}

// Metro Express, 3.3V
float getVoltage3V(int pin){
 // 3.3V/1023
 return (analogRead(pin) * 0.003225806452); 
}
