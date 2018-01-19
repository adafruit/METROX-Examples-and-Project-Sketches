// CIRC13 - Squeezing

int sensePin = 2; // the pin the FSR is attached to
int ledPin = 9; // the pin the LED is attached to (use one capable of PWM)
void setup() {
 Serial.begin(9600);
 pinMode(ledPin, OUTPUT); // declare the ledPin as an OUTPUT
}
void loop() {
 int value = analogRead(sensePin) / 4; //the voltage on the pin divded by 4 (to
 //scale from 10 bits (0-1024) to 8 (0-255)
 analogWrite(ledPin, value); //sets the LEDs intensity proportional to
 //the pressure on the sensor
 Serial.println(value); //print the value to the debug window
}
