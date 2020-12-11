/*
 * CIRC18 Make It Better
 * NeoPixel Glance Thermometer - check the weather super quickly!
 * 
 * by Brent Rubell for Adafruit Industries
*/

 // Include the Adafruit Neopixel Library 
#include <Adafruit_NeoPixel.h>

// The default pin for the NeoPixel on the Metro Express is Pin #40
#define METROPIXELPIN            40

// Temperature Sensor
const int temperaturePin = A0; 

// metroPixel takes in both the number of pixels (1, the built-in) and the pin)
Adafruit_NeoPixel metroPixel = Adafruit_NeoPixel(1, METROPIXELPIN);
float temperature = 0;

/* Temperature Colors */
const int RED[ ] = {255, 0, 0};
const int ORANGE[ ] = {255, 153, 51};
const int YELLOW[ ] = {255, 255, 0};
const int LIGHTGREEN[ ] = {128, 255, 0};
const int DARKGREEN[ ] = {76, 153, 0};
const int DARKBLUE[ ] = {0, 0, 255};
const int DARKPURPLE[ ] = {51, 0, 102};
const int BLACK[ ] = {0, 0, 0};

void setup()
{
  // Start the Serial at 9600 baud
  Serial.begin(9600);
  // init the neopixel library   
  metroPixel.begin();
}
 
void loop()                     
{
 temperature = getVoltage3V(temperaturePin);
 // Convert to degrees C
 temperature = (temperature - .5) * 100;          
 // print the temperature in C to the serial                                                
 Serial.println(temperature); 
 // temp <-> color picker       
 if (temperature > 40) {
  // red
  pixelWrite(RED);
 }
 else if (temperature > 35) {
   // orange
   pixelWrite(ORANGE);
 }
 else if (temperature > 30) {
   // yellow
   pixelWrite(YELLOW);
 }
 else if (temperature > 25) {
   // light green
   pixelWrite(LIGHTGREEN);
 }
 else if (temperature > 20) {
   // dark green
   pixelWrite(DARKGREEN);
 }
 else if (temperature > 5) {
   // dark blue
   pixelWrite(DARKBLUE);
 }
 else {
   // dark purple
   pixelWrite(DARKPURPLE);
 }
 delay(1000);                                     
}

// takes in a pre-defined color (integer array) and sets the pixel to that color
void pixelWrite(const int* color) { 
  metroPixel.setPixelColor(0, metroPixel.Color(color[0],color[1],color[2]));
  // write the pixel color to the Metro's Neopixel
  metroPixel.show(); 
}

// Voltage to temperature if Vs= 3.3V
float getVoltage3V(int pin){
 // 3.3V/1023
 return (analogRead(pin) * 0.003225806452); 
}
