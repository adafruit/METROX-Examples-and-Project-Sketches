/*
 * PROJ08: Analog Temperature Gauge
 * for the MetroX Classic and Express Guide
 * 
 * by Brent Rubell and Asher Lieber for Adafruit Industries.    Support Open Source, buy Adafruit!
 */
#include <Servo.h>

#define ANALOGREFVOLTAGE 5.555
 
// TMP36 Pin 
const int temperaturePin = A0;

// create servo object to control the analog gauge
Servo metroServo;
// pulse width (uS) corresponding to 0 on the servo
const int servoMin = 544;
// pulse width (uS) corresponding to 180 on the servo
const int servoMax = 2400;

int servoPos = 0;

void setup() {
  // start the serial connection
  Serial.begin(9600);
  // attach a servo at pin 9 with movement constraints
  metroServo.attach(9, servoMin, servoMax);
}

void loop() {
  // read the voltage from the pin
  float voltage = getVoltage(temperaturePin);

  
  // convert the voltage to a temperature value
  float temperature = convertToF(voltage);

  /* We're going to take in the Temperature and map it to a servo value:
   *  Minimum Temperature Value: -10 (you can change this!)
   *  Maximum Temperature Value: 100 (you can change this, too)
   *  If your temp is -10, the servo will move to 0 degrees
   *  also, if your temp is 100, the servo will move to 180 degrees
   *  ...everything else will be mapped between the range
   */
  servoPos = map((int(temperature)), 0, 100, 0, 180);
  // write servoPos to the servo
  metroServo.write(servoPos);
  // poll every minute
  delay(60000);

}

// gets the voltage from the analog pin
float getVoltage(int pin) { 
  return(float(analogRead(pin))* float(ANALOGREFVOLTAGE/1023.000));  
}

// convert C to F
float convertToF(float voltage) {
  return (((voltage - .5) * 100)*1.8) + 32;
}

// convert F to C
float convertToC(float voltage) {
  return (voltage - 0.5) * 100;
}
