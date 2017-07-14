/*
 * Experimenter's Guide for Metro (and Metro Express!)
 * CIRC14: Digital Thermometer
 * Desc: Checks temp. with a TMP36 and prints it to a 16x2 character lcd
 * adafruit industries ~ Support Open Source, buy adafruit!
 * Date: June 2017
 */

/* Metro/Metro Express Select
   Set which board you own to true
*/ 
// I have a Metro
#define Metro false
// I have a Metro EXPRESS 
#define MetroExpress false

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

  if(Metro == true) {
    temperature = getVoltage5V(temperaturePin);
    Serial.println(temperature);
  }
  else if(MetroExpress == true) {
    temperature = getVoltage3V(temperaturePin);
    Serial.println(temperature);
  }
  else if(MetroExpress == false and Metro == false) {
    Serial.println("Error, please select a board");
  }

  
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
