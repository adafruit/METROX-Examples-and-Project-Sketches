/*
 * (PROJ02) Metro (and Metro Express!) Fidget Spinner Tachometer
 * Desc: Count fidget spinner RPMs (and beat your high scores)
 * 
 * Original code by Tony Dicola for Adafruit Industries
 * by Brent Rubell and Asher Lieber for the Metro Explorers Guide
*/

// include the LCD library code:
#include <LiquidCrystal.h>
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

// How many arms does the spinner have?
#define SPINNER_ARMS         3
// 1kB sample size
#define SAMPLE_DEPTH        256
// delay between light samples
#define SAMPLE_PERIOD_US   150
// min. speed, depends on reflective-ness of spinner, noise thresh.
//#define THRESHOLD           127
// wait 2s between measurements
#define MEASURE_PERIOD_MS  2000

// rpm high score
float rpmHighScore = 0.00;
// threshold value
int threshold;
// photo light sensor pin
int photoSensor = A0;
// led pin
int led = 2;

void setup() {
  // Init. serial monitor @ 115200 baud
  Serial.begin(9600);
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  lcd.print("Metro Tachometer");
  // set up LED
  pinMode(led, OUTPUT);
}

void loop() {
  int sensorCalibrate = 0; 
  // Set depending on light balance
  threshold = 40;

  // PAUSE between measurements 
  lcd.clear();
  lcd.print("GET READY...");
  analogWrite(led, 255);

  // pause between sampling sensor
  // shown as a countdown on the screen! 
  for (int i = 3500; i > 0; i--) {
    lcd.setCursor(0,1);
    lcd.print(i/100);
  }
  
  
  // init. empty sample array
  uint16_t samples[SAMPLE_DEPTH] = {0};
  // start time
  uint32_t start = micros();

  // lcd during spin
  lcd.clear();
  lcd.print("SPIN IT");
  lcd.setCursor(0,1);
  lcd.print("score: ");
  lcd.setCursor(10,1);
  lcd.print(rpmHighScore);
  
  for (int i = 0; i < SAMPLE_DEPTH; i++) {
    // sample the photo light sensor
    samples[i] = analogRead(photoSensor);
    // serial output
    Serial.print("\nSample: ");
    Serial.print(samples[i]);
    // keep the player occupied while sampling
    if (i == int(SAMPLE_DEPTH/4)) {
      lcd.clear();
      lcd.print("keep going!");
      lcd.setCursor(10,1);
      lcd.print(rpmHighScore);
    }
    else if (i == int(SAMPLE_DEPTH/3)) {
     lcd.clear();
     lcd.print("almost there!");
     lcd.setCursor(10,1);
     lcd.print(rpmHighScore);
    }

    delayMicroseconds(SAMPLE_PERIOD_US);
  }
  
  // time elapsed (uS)
  uint32_t elapsed_uS = micros() - start;
  // time elapsed (sec)
  float elapsed = elapsed_uS / 1000000.0; 


  // Find the min and max values in the collected samples.
  uint16_t minval = samples[0];
  uint16_t maxval = samples[0];
  for (int i=1; i<SAMPLE_DEPTH; ++i) {
    minval = min(minval, samples[i]);
    maxval = max(maxval, samples[i]);
  }

  // Serial Monitor Values 
  Serial.print("\n Samples taken, : ");
  Serial.print(elapsed, 3);
  Serial.print(" seconds");
  Serial.print("\n Max Sample Val: ");
  Serial.print(maxval);
  Serial.print("\n Min Sample Val: ");
  Serial.print(minval);

  // Check the amplitude of the signal (difference between min and max)
  // is greater than the threshold to continue detecting speed.
  uint16_t amplitude = maxval - minval;
  if (amplitude < threshold) {
    // Didn't make it past the threshold so start over with another measurement attempt.
    lcd.clear();
    lcd.println("didnt spin fast enough, re-spin!");
    Serial.print("\n DIDNT PASS THRESHOLD, RE-TAKING MEASUREMENT..");
    return;
  }

  // Compute midpoint of the signal (halfway between min and max values).
  uint16_t midpoint = minval + (amplitude/2);

  // Count how many midpoint crossings were found in the signal.
  // These are instances where two readings either straddle or land on
  // the midpoint.  The midpoint crossings will happen twice for every
  // complete sine wave cycle (once going up and again coming down).
  int crossings = 0;
  for (int i=1; i<SAMPLE_DEPTH; ++i) {
    uint16_t p0 = samples[i-1];
    uint16_t p1 = samples[i];
    if ((p1 == midpoint) || 
        ((p0 < midpoint) && (p1 > midpoint)) ||
        ((p0 > midpoint) && (p1 < midpoint))) {
      crossings += 1;
    }
  }
  
  // Compute signal frequency, RPM, and period.
  // The period is the amount of time it takes for a complete
  // sine wave cycle to occur.  You can calculate this by dividing the
  // amount of time that elapsed during the measurement period by the
  // number of midpoint crossings cut in half (because each complete
  // sine wave cycle will have 2 midpoint crossings).  However since
  // fidget spinners have multiple arms you also divide by the number
  // of arms to normalize the period into a value that represents the
  // time taken for a complete revolution of the entire spinner, not
  // just the time between one arm and the next.

  Serial.print("\n MP Crossings: ");
  Serial.print(crossings);
  Serial.print("\n Elapsed: ");
  Serial.print(elapsed);
  
  float period = elapsed / (crossings / 2.0 / SPINNER_ARMS);
  
  Serial.print("\n Period: ");
  Serial.print(period);

  // Once the period is calculated it can be converted into a frequency
  // value (i.e revolutions per second, how many times the spinner spins
  // around per second) and more common RPM value (revolutions per minute,
  // just multiply frequency by 60 since there are 60 seconds in a minute).
  float frequency = 1.0 / period;
  float rpm = frequency * 60.0;

  
  // Print out the measured values!
  Serial.print("Frequency: ");
  Serial.print(frequency, 3);
  Serial.print(" (hz)\t\tRPM: ");
  Serial.print(rpm, 3);
  Serial.print("\t\tPeriod: ");
  Serial.print(period, 3);
  Serial.println(" (seconds)");


  lcd.clear();
  lcd.setCursor(1,0);
  lcd.print(rpm);
  delay(2000);
  
  // high score checker 
  if(rpm > rpmHighScore) {
    rpmHighScore = rpm;
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("you beat the");
    lcd.setCursor(0,1);
    lcd.print("high score!");
    delay(2000);
    
  }

}
