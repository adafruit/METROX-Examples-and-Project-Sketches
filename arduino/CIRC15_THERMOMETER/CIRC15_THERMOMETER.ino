/*
 * CIRC15: Digital Thermometer
 * Experimenter's Guide for Metro (and Metro Express!)
 *  by Brent Rubell for Adafruit Industries ~ Support Open Source, buy adafruit!
 */

// If you're using a METRO EXPRESS, change this value to 3.333
#define ANALOGREFVOLTAGE 5.000

// include the lcd library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

// TMP36 Pin 
int temperaturePin = 0;

void setup() {
  Serial.begin(9600);
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
}

void loop() {
  
  float temperature = 0;
  temperature = getVoltage(temperaturePin);
  
  /* Output: Degrees C */
  temperature = (temperature - .5) * 100; 
  /* Output: Degrees F */
  // temperature = (((temperature - .5) * 100)*1.8) + 32;
  /* Output: Voltage */
  // temperature = (temperature - .5) * 100; d
  
  // Write temperature to the LCD
  lcd.print("Temp: ");
  lcd.setCursor(6,0);
  lcd.print(temperature);
  lcd.setCursor(11,0);
  lcd.print("*C");
  // Wait 1s
  delay(1000);
  // Refresh the LCD
  lcd.clear();
}

float getVoltage(int pin) { 
  return(float(analogRead(pin))* float(ANALOGREFVOLTAGE/1023.000));  
}
