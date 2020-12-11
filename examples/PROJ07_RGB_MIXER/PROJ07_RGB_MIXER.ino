/* 
 *  PROJ07 - RGB Color Mixer
 *  
 *  by Brent Rubell for Adafruit Industries
 */

// RGB LED Pins
int rgbLED[] = {9, 10, 11};

// trim potentiometer pin
int trimPin = A0;
// button pin 
const int buttonPin = 12;

// button state
int buttonState = 0;
// trim pot. value
int trimValue = 0;


int colorIdx = 0;
int red = 0;
int green = 0;
int blue = 0;

boolean CURRENTRGB[] = {0, 0, 0};

void setup() {
  // Setup Serial
  Serial.begin(9600);
  // set the 3 pins as output pins
  for(int i = 0; i < 3; i++) {
    pinMode(rgbLED[i], OUTPUT);
  }
  // initialize the push-button as an input
  pinMode(buttonPin, INPUT);
}

void loop() {
  // read the value of the push-button 
  buttonState = digitalRead(buttonPin);
  
  if(buttonState == LOW) {
    delay(2);
    // reset the colorIdx if it goes past Blue (colorIdx = 3)
    if(colorIdx == 3) {
      colorIdx = 0;
    }
    colorIdx++;
    switch(colorIdx) {
      case 1:
        trimValue = analogRead(trimPin);
        red = map(trimValue, 0, 670, 0, 255);
        CURRENTRGB[0] = red;
        break;
      case 2: 
        trimValue = analogRead(trimPin);
        green = map(trimValue, 0, 670, 0, 255);
        CURRENTRGB[1] = green;
        break;
      case 3: 
        trimValue = analogRead(trimPin);
        blue = map(trimValue, 0, 670, 0, 255);
        CURRENTRGB[2] = blue;
        break;
      default:
        break;
    }

    Serial.println("red:");
    Serial.print(CURRENTRGB[0]);
    Serial.println(" ");

    Serial.println("green:");
    Serial.print(CURRENTRGB[1]);
    Serial.println(" ");

    Serial.println("blue:");
    Serial.print(CURRENTRGB[2]);
    Serial.println(" ");
  
    setColor(rgbLED, CURRENTRGB);
    delay(1000);

    
  }
  
}

void setColor(int* led, const boolean* color) {
  for(int i = 0; i < 3; i++){
    digitalWrite(led[i], color[i]);
  }
}
