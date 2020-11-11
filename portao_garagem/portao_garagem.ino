#include <Servo.h>
Servo myservo;
char leitura;
int pos = 0;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {
  myservo.write(0);
  while (Serial.available()) {
    leitura = Serial.read();
    if (leitura == 'O') {
      digitalWrite(13, HIGH);
      myservo.write(180);
      delay(5000);
    }
    else if (leitura == 'C') {
      myservo.write(0);
      digitalWrite(13, LOW);
      delay(7000);
    }
    else Serial.end(); // Fim da conexão
  }
}
