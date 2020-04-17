
int val = 0;
int i = 0;
float temperaturec = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {

  long sum = 0;

  // put your main code here, to run repeatedly:
  for(i = 0; i<100; i++){
    val = analogRead(0);
    sum = sum + val;
  }
  
  float avg = sum/100.0;
  temperaturec = .1008 * avg - 26.361;
  float tempf = (9.0/5.0)*temperaturec+32.0;
  
  Serial.print("Analog = ");
  Serial.print(avg);
  Serial.print("     Temperature (C) = ");
  Serial.print(temperaturec);
  Serial.print("     Temperature (F) = ");
  Serial.print(tempf);
  Serial.println();
}
