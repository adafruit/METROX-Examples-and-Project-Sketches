// CIRC14 - Character LCDs

// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
// modified for Metro Explorers Guide
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("hello, world!");
}

void loop() {

}
