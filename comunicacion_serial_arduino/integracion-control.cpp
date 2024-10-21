#define calefactor 10

int pwm = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(calefactor, OUTPUT);
  analogWrite(calefactor, 0);
  String valueOutput = "";
}

void loop()
{
  if (Serial.available() > 0) {
    
    while (Serial.available()) {
        char c = Serial.read();
        message += c;
        delay(10);
    }
    analogWrite(calefactor, valueOutput.toInt());
    Serial.println(valueOutput);
    valueOutput = "";
  }
}