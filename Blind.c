# include<Arduino.h>
#define trigPin 9
#define echoPin 10
#define buzzer 8
long duration;
int distance;
void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  Serial.print("Distance: ");
  Serial.println(distance);
  if (distance <= 20) {
    digitalWrite(buzzer, HIGH);  // Continuous sound (very close)
  } 
  else if (distance > 20 && distance <= 50) {
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(buzzer, LOW);
    delay(200); // Slow beep
  } 
  else {
    digitalWrite(buzzer, LOW); // No obstacle
  }

  delay(100);
}