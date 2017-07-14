/* CIRC10.5: Temperature Alarm
 *  (bonus circuit for MetroX)
 *  
 *  by Adafruit Industries
 */


/* Metro/Metro Express Select
Set which board you own to true
*/ 
// I have a Metro
#define Metro false
// I have a Metro EXPRESS 
#define MetroExpress true

// TMP36 Pin 
int temperaturePin = 0;

// Piezo Pin 
int piezoPin = 8;
// Freezing
float freezeTemp = 0;
// Boiling
float boilTemp = 26;


void setup()
{
// Start the Serial connection
Serial.begin(9600); 
}

void loop() // run over and over again
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

if(temperature < freezeTemp) {
tone(piezoPin, 1100, 1000);
}
else if(temperature > boilTemp) {
tone(piezoPin, 1100, 1000);
}

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
