// CIRC16 - IR Sensor 

// include all IRLib 2.x libraries
#include <IRLibAll.h>

// These values are for the Adafruit Mini Remote (using the NEC Protocol)
#define MY_PROTOCOL NEC
// Handles NEC repeat codes
uint32_t Previous;
// button(s)
#define BUTTON_0 0xfd30cf
#define BUTTON_1 0xfd08f7
#define BUTTON_2 0xfd8877
#define BUTTON_3 0xfd48b7
#define BUTTON_4 0xfd28d7
#define BUTTON_5 0xfda857
#define BUTTON_6 0xfd6897
#define BUTTON_7 0xfd18e7
#define BUTTON_8 0xfd9867
#define BUTTON_9 0xfd58a7

// pin for the reciever
IRrecv myReceiver(6);
// decoder class
IRdecode myDecoder;

// LED PIN
int ledPin = 13;

void setup() {
  // set the ledPin as an output
  pinMode(ledPin, OUTPUT);
  // enable the receiver
  myReceiver.enableIRIn();
}

void loop() {
  // if the receiver gets a signal
  if(myReceiver.getResults()) {
    // decode the signal
    myDecoder.decode();
    // set the decoder's protocol to the set protocol
    if(myDecoder.protocolNum == MY_PROTOCOL) {
      // if there
      if(myDecoder.value == 0xFFFFFFFF) {
        // keep the led set to the last button value
        myDecoder.value = Previous;
      }
      // based on myDecoder.value, switch between button codes
      switch(myDecoder.value) {
        // Turn on the LED
        case BUTTON_1:
          digitalWrite(ledPin, HIGH);
          break;
        // otherwise, turn off the LED
        default:
          digitalWrite(ledPin, LOW);
          break;
      }
      // keep the LED set to the last button value
      Previous = myDecoder.value;
    }
    // enable the IR receiver
    myReceiver.enableIRIn();
  }
}

// sets the color of the RGB LED
void setColor(int* led, const boolean* color) {
  for(int i = 0; i < 3; i++) {
    digitalWrite(led[i], color[i]);
  }
}
