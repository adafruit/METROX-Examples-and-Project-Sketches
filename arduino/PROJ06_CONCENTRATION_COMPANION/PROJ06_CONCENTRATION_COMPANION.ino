/*
 * Metro Explorers Guide
 * PROJ07: Concentration Companion 
 * by Brent Rubell and Asher Lieber for Adafruit Industries.   Support Open Source, buy Adafruit!
 * 
 */

/* Set the input you're using to True */ 
#define BUTTON  False
#define FSR     False
#define TRIM    False
#define IR      True 

/* Input Pinouts */
const int pushbtn = 3; 
const int fsr = A2;
const int trimpot = A0;
const int irSensor = 6;

/* RGB LED Pin Config
   9 = RED, 10 = GREEN, 11 = BLUE
*/
int rgbLED[] = {9, 10, 11};
// MetroX comes with a common anode RGB LED (if you have another RGB LED, this will be different)
// let on be low
const boolean ON = LOW;
// let off be high
const boolean OFF = HIGH;

/* Csikszentmihályi's Flow Model Colors */
const boolean ANXIETY[] = {ON, OFF, OFF}; 
const boolean RELAXATION[] = {OFF, ON, OFF};
const boolean APATHY[] = {OFF, OFF, ON}; 
const boolean FLOW[] = {ON, ON, OFF}; 
const boolean CYAN[] = {OFF, ON, ON}; 
const boolean WORRY[] = {ON, OFF, ON}; 
const boolean CONTROL[] = {ON, ON, ON}; 

// flow
const int flow[ ] = {ANXIETY};

void setup() {
   // set the RGB LED as an output
  for(int i = 0; i < 3; i++) {
    pinMode(rgbLED[i], OUTPUT);
  }
  // set input mode depending on what type of input you're using
  #ifdef BUTTON
    pinMode(pushbtn, INPUT);
  #elif FSR
    pinMode(fsr, INPUT);
  #elif TRIM 
    pinMode(trimpot, INPUT);
  #elif IR
    pinMode(irSensor, INPUT);
  #endif

}

void loop() {

  #ifdef BUTTON
    if(buttonState == HIGH) {
      setColor(ledDigitalOne, 
    }
  #endif
  setColor(ledDigitalOne, CYAN);
}

void setColor(int* led, const boolean* color) {
  for(int i = 0; i < 3; i++){
    digitalWrite(led[i], color[i]);
  }
