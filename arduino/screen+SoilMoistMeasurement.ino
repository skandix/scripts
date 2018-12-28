#include <LiquidCrystal.h>

int sensorPin = A0;  
int sensorValue = 0;  
int percent = 0;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int convertToPercent(int value)
{
  int percentValue = 0;
  percentValue = map(value, 1023, 465, 0, 100);
  return percentValue;
}

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
}

void loop() {
  lcd.setCursor(0, 1);
  sensorValue = analogRead(sensorPin);
  percent = convertToPercent(sensorValue);
  lcd.print(percent);
  delay(1000);
}
