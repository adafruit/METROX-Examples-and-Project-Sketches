// PROJ03 - Music Box

// include the lcd library code
#include <LiquidCrystal.h>
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

// Piezo code.
int speakerPin = 5;
int length = 15; // the number of notes
char notes[] = "ccggaagffeeddc "; // a space represents a rest
int beats[] = { 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 };
int tempo = 300;

// Photo Light Sensor Pin
int lightPin = 0;
// Measured Darkness
int dark = 650;

// LCD Backlight Pin
int backlightPin = 13;

void playTone(int tone, int duration) {
  for (long i = 0; i < duration * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}

void playNote(char note, int duration) {
  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };

  // play the tone corresponding to the note name
  for (int i = 0; i < 8; i++) {
    if (names[i] == note) {
      playTone(tones[i], duration);
    }
  }
}

void setup() {
   // set up the serial monitor
   Serial.begin(9600);
   // set up the LCD's cols/rows
   lcd.begin(16, 2);
   // set speaker as an output
   pinMode(speakerPin, OUTPUT);
   // set lcd backlight as an output
   pinMode(backlightPin, OUTPUT);

}

void loop() {
  // read the lightLevel
  int lightLevel = analogRead(lightPin);
  Serial.println("Light Level -> ");
  Serial.println(lightLevel);

  // check lightLevel against dark level (should be set manually by the user, check serial mon.)
  if(lightLevel < dark)
  {
    // Box is OPEN!
    digitalWrite(backlightPin, HIGH);
    lcd.clear();
    Serial.println("Box open, playing music!");
    for (int i = 0; i < length; i++) {
      if(notes[i] == ' ') {
        // rest
        delay(beats[i] * tempo);
        // print a space to indicate a rest
        lcd.print(" ");
      }
      else {
        // play notes in notes[]
        playNote(notes[i], beats [i] * tempo);
        // display current note on the lcd
        lcd.print(notes[i]);
      }
      // pause between notes
      delay(tempo/2);
    }
  }
  else{
    // box is closed
    // turn LCD off
    digitalWrite(backlightPin, LOW);
    lcd.clear();
    lcd.print("box closed...");
    Serial.println("Box closed, don't play music.");
  }
}
