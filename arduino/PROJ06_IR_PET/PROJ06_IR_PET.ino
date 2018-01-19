// PROJ06 - IR Pet Toy

#include <IRLibAll.h>
#include <Servo.h>

/* Adafruit Mini Remote */
#define MY_PROTOCOL NEC
#define RIGHT_ARROW   0xfd50af
#define LEFT_ARROW    0xfd10ef
#define SELECT_BUTTON 0xfd906f
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
// pin number for the receiver
IRrecv myReceiver(2);
IRdecode myDecoder;
// handles nec repeat codes
uint32_t Previous;

/* Servo */
// create a servo object
Servo myServo;
// stores the servo position
int16_t pos;
// angle (degrees) to move the servo left/right
int16_t Speed;

void setup() {
  // randomizes a seed for random() calls
  randomSeed(analogRead(0));
  // set the laser pin as an output
  //pinMode(laserPin, OUTPUT);
  // attach servo to pin 9
  myServo.attach(9);
  // set initial position
  pos = 90;
  // set initial speed
  Speed = 5;
  // write initial pos to servo at startup
  myServo.write(pos);
  // Start the IR receiver
  myReceiver.enableIRIn();
}

void loop()
{
  if (myReceiver.getResults()) {
    myDecoder.decode();
    if (myDecoder.protocolNum == MY_PROTOCOL) {
      if (myDecoder.value == 0xFFFFFFFF)
        myDecoder.value = Previous;
      switch (myDecoder.value) {
        case LEFT_ARROW:
          // move servo
          pos = min(180, pos + Speed);
          break;
        case RIGHT_ARROW:
          pos=max(0,pos-Speed);
          break;
        case BUTTON_0:
          pos=random(0,180);
          break;
        }
       // tell servo 'move to variable pos'
       myServo.write(pos);
       Previous=myDecoder.value;
      }
    myReceiver.enableIRIn();
  }
}
