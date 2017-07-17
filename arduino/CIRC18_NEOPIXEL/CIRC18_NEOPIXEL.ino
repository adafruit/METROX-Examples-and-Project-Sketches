/*
 * (CIRC18) Metro Express NeoPixel 
 * this circuit was designed for use with the Metro Explorers Guide on Learn.Adafruit.com
 * 
 * note: this code does NOT run on the Metro, only the Metro EXPRESS. 
 * 
 * by Brent Rubell for Adafruit Industries.
 */

// Include the Adafruit Neopixel Library 
#include <Adafruit_NeoPixel.h>

// The default pin for the NeoPixel on the Metro Express is Pin #40
#define METROPIXELPIN            40

// metroPixel takes in both the number of pixels (1, the built-in) and the pin)
Adafruit_NeoPixel metroPixel = Adafruit_NeoPixel(1, METROPIXELPIN);

/* Colors */ 
// note: the max. of colors in these arrays is 220 instead of 255 (super-bright!!)
const int RED[ ] = {155, 0, 0};
const int WHITE[ ] = {155, 155, 155};
const int BLUE[ ] = {0, 0, 255};
const int BLACK [ ] = {0, 0, 0};

void setup() {
  // init. the NeoPixel library 
  metroPixel.begin(); 
}

void loop() {
  // display red on the Metro Express neopixel
  pixelWrite(RED);
  delay(20);
  // display white on the Metro Express neopixel
  // this is a HTML color picker format, if you want to use it (see: https://www.w3schools.com/colors/colors_picker.asp)
  metroPixel.setPixelColor(0, 0xFF0000); 
  delay(20);
  // display blue on the Metro Express neopixel
  pixelWrite(BLUE);
  delay(20);
  
  // Sparkle the Neopixel 
  // pixelSparkle();
}

// takes in a pre-defined color (integer array) and sets the pixel to that color
void pixelWrite(const int* color) { 
  metroPixel.setPixelColor(0, metroPixel.Color(color[0],color[1],color[2]));
  // write the pixel color to the Metro's Neopixel
  metroPixel.show(); 

}

// flashes the neopixel on and off rapidly 
void pixelSparkle() { 
  for(int i = 0; i < 5; i++) {
    pixelWrite(BLACK);
    delay(50);
    pixelWrite(WHITE);
    delay(50);
  }
}











