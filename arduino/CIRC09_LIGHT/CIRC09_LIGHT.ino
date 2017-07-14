/*
 * CIRC09 - Metro Photo Light Sensor
 * Desc - Changes the intensity of a LED based on the amount of light 
 * incident on the photo light sensor.
 */

 // photo light sensor
 int lightPin = 0;
 // LED pin
 int ledPin = 9;

 void setup()
{
  // set the led pin to output
  pinMode(ledPin, OUTPUT); 
}

void loop()
{
  // read in the light level
  int lightLevel = analogRead(lightPin); 
  // map the lightlevel to 0<=lightLevel<=255
  lightLevel = map(lightLevel, 0, 900, 0, 255);
  // constrain between 0 and 255
  lightLevel = constrain(LightLevel, 0, 255);
  // write lightLevel to the LED
  analogWrite(ledPin, lightLevel);
}
