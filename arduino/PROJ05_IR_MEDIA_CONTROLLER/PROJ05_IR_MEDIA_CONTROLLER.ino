// PROJ05 - IR Media Controller

#include <IRLibAll.h>
#include <Keyboard.h>

/* Remote Codes */
#define VOLUMEUP      0xfd40bf
#define VOLUMEDOWN    0xfd00ff
#define RIGHT_ARROW   0xfd50af
#define LEFT_ARROW    0xfd10ef
#define PLAYPAUSE     0xfd807f
#define SELECT_BUTTON 0xfd906f
// These are some extra button codes...not used in the PROJ.
// if you want to create more functions in VLC or any other app, use these!
#define UP_ARROW      0xfda05f
#define DOWN_ARROW    0xfdb04f
#define BUTTON_0      0xfd30cf
#define BUTTON_1      0xfd08f7
#define BUTTON_2      0xfd8877
#define BUTTON_3      0xfd48b7
#define BUTTON_4      0xfd28d7
#define BUTTON_5      0xfda857
#define BUTTON_6      0xfd6897
#define BUTTON_7      0xfd18e7
#define BUTTON_8      0xfd9867
#define BUTTON_9      0xfd58a7
// Adafruit Mini-Remote uses NEC, change this if you're using a different remote
#define MY_PROTOCOL NEC

// receiver on pin 2
IRrecv myReceiver(2);
// Decoder object
IRdecode myDecoder;

// NEC repeat codes for Adafruit Mini-Remote
uint32_t Previous;

// use this option for OSX:
char ctrlKey = KEY_LEFT_GUI;
// use this option for Windows and Linux:
//  char ctrlKey = KEY_LEFT_CTRL;

const int ledPin = 13;

void setup() {
  // monitor the serial at 9600baud
  Serial.begin(9600);
  // initialize control over the keyboard
  Keyboard.begin();
  // start the IR receiver
  myReceiver.enableIRIn();
  // configure status LED
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.println("Listening to IR...");
}

void loop()
{
    if (myReceiver.getResults()) {
       myDecoder.decode();
       if(myDecoder.protocolNum==MY_PROTOCOL) {
         if(myDecoder.value==0xFFFFFFFF)
           myDecoder.value=Previous;
         // We used VLC for this example, but you can use any keyboard shortcuts!
         // (src: https://wiki.videolan.org/Hotkeys_table/)
         switch(myDecoder.value) {
           case PLAYPAUSE:
            // key-play-pause
            // send the spacebar key
            Keyboard.write((char)0x20);
            digitalWrite(LED_BUILTIN, HIGH);
            delay(100);
            // release the keys pressed
            Keyboard.releaseAll();
            break;
           case VOLUMEUP:
            // key-vol-up
            // vlc shortcut: ctrl + up arrow
            Keyboard.press(ctrlKey);
            Keyboard.press(KEY_UP_ARROW);
            digitalWrite(LED_BUILTIN, HIGH);
            delay(100);
            Keyboard.releaseAll();
            break;
          case VOLUMEDOWN:
            // key-vol-down
            // vlc shortcut: ctrl + down arrow
            Keyboard.press(ctrlKey);
            Keyboard.press(KEY_DOWN_ARROW);
            digitalWrite(LED_BUILTIN, HIGH);
            delay(100);
            Keyboard.releaseAll();
            break;
          case RIGHT_ARROW:
            // key-faster
            // vlc shortcut: +
            Keyboard.press('+');
            digitalWrite(LED_BUILTIN, HIGH);
            delay(100);
            Keyboard.releaseAll();
            break;
          case LEFT_ARROW:
            // key-faster
            // vlc shortcut: -
            Keyboard.press('-');
            digitalWrite(LED_BUILTIN, HIGH);
            delay(100);
            Keyboard.releaseAll();
            break;
          default:
            // if nothing else matches, do the default
            // default is optional
            break;
         }
         Previous=myDecoder.value;
       }
       digitalWrite(LED_BUILTIN, LOW);
       myReceiver.enableIRIn();
    }
}
