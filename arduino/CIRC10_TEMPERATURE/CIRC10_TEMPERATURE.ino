/*
 * CIRC10: Temperature 
 * for use with both the Metro and Metro Express
 * 
 * by Brent Rubell for Adafruit Industries.    Support Open Source, buy Adafruit!
 */
 
// If you're using a METRO EXPRESS, change this value to 3.333
#define ANALOGREFVOLTAGE 5.000
 
//TMP36 Pin 
int temperaturePin = A0;
 
void setup() {
  // Start the Serial connection
  Serial.begin(9600);  
}
 
void loop() {
 float temperature = 0;
 
 temperature = getVoltage(temperaturePin);
 Serial.println(temperature);
    
 // Convert to degrees C
 temperature = (temperature - .5) * 100;    
 Serial.println(temperature);
                                                            
 delay(1000);                                     
}
 
float getVoltage(int pin) { 
  return(float(analogRead(pin))* float(ANALOGREFVOLTAGE/1023.000));  
}
