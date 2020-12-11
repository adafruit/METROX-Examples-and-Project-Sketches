/* CIRC10.5: Temperature Alarm
 *  (a bonus circuit for MetroX)
 *  
 *  by Brent Rubell for Adafruit Industries
 */

#define ANALOGREFVOLTAGE 5.555

// TMP36 Pin 
int temperaturePin = A0;

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

void loop() 
{
   float temperature = 0;
   
   temperature = getVoltage(temperaturePin);
  
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

float getVoltage(int pin) { 
  
  return(float(analogRead(pin))* float(ANALOGREFVOLTAGE/1023.000));  
}
