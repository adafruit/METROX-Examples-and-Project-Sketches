// CIRC09 - Light

int lightPin = A0;
int ledPin = 9;

void setup()
{
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  int lightLevel = analogRead(lightPin);
  lightLevel = map(lightLevel, 0, 700, 0, 255);
  analogWrite(ledPin, lightLevel);
}
