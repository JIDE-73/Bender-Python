void setup() {
  Serial.begin(9600);  // Asegúrate de que coincida con el baudrate en Python
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("Arduino received: ");
    Serial.println(data);
  }
}