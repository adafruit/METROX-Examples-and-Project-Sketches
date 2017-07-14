//  RGB LED PINS
// three pins:
// 9 = RED
// 10 = GREEN
// 11 = BLUE
int ledDigitalOne[] = {9, 10, 11};

// define on as low 
// (because you use a common anode RGB LED)
const boolean ON = LOW;
// define off as high
const boolean OFF = HIGH;

//  Predefined Colors 
const boolean RED[] = {ON, OFF, OFF}; 
const boolean GREEN[] = {OFF, ON, OFF};
const boolean BLUE[] = {OFF, OFF, ON}; 
const boolean YELLOW[] = {ON, ON, OFF}; 
const boolean CYAN[] = {OFF, ON, ON}; 
const boolean MAGENTA[] = {ON, OFF, ON}; 
const boolean WHITE[] = {ON, ON, ON}; 
const boolean BLACK[] = {OFF, OFF, OFF};

//An Array that stores the predefined colors
const boolean* COLORS[] = 
  {RED, GREEN, BLUE,YELLOW, CYAN, MAGENTA, 
  WHITE, BLACK};

void setup() {
  for(int i = 0; i < 3; i++){
    //  set the 3 pins as outputs
    pinMode(ledDigitalOne[i], OUTPUT);
  }
}

void loop() {
  // set the color of the LED
  setColor(ledDigitalOne, CYAN);
  // randomize it
  // randomColor();
}

void randomColor(){
  //  get random number within range of colors
  int rand = random(0, sizeof(COLORS) / 2);
  setColor(ledDigitalOne, COLORS[rand]);
  delay(1000);
}

void setColor(int* led, const boolean* color) {
  for(int i = 0; i < 3; i++){
    digitalWrite(led[i], color[i]);
  }
}
