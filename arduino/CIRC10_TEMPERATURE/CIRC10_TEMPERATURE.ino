// CIRC10 - Temperature

#define ANALOGREFVOLTAGE 5.555

//TMP36 Pin
int temperaturePin = A0;

void setup() {
  // Start the Serial connection
  Serial.begin(9600);
}

void loop() {
 float temperature = 0;

 temperature = getVoltage(temperaturePin);
 Serial.println(temperature);

 // Convert to degrees C
 temperature = (temperature - .5) * 100;
 Serial.println(temperature);

 delay(1000);
}

float getVoltage(int pin) {

  return(float(analogRead(pin))* float(ANALOGREFVOLTAGE/1023.000));
}
