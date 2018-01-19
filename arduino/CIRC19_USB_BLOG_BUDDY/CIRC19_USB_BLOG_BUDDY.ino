// CIRC19 - Adding USB-HID Control

// include the mouse library
#include <Mouse.h>

// trimpot pin
const int trimPin = A0;

// button pin
const int buttonPin = 2;

// reduces scrolling speed (ms)
const int scrollDelay = 100;

// trimpot value
int trimValue = 0;

// button state
int buttonState = 0;

void setup() {
  // start serial monitor at 9600 baud
  Serial.begin(9600);
  // start the mouse
  Mouse.begin();
}

void loop() {
  // read the button state
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    // stop the mouse if button not pressed
    Mouse.end();
  }
  else {
    // start the mouse (if stopped)
    Mouse.begin();
    // read the trimpot value
    trimValue = analogRead(trimPin);
    // map the trimValues to scroll wheel down (-neg values) and up (+pos values)
    trimValue = map(trimValue, 0, 1023, -5, 5);
    // move the mouse wheel (dont change cursor position)
    Mouse.move(0, 0, trimValue);
    // reduce the scrolling speed
    delay(scrollDelay);
  }
}
