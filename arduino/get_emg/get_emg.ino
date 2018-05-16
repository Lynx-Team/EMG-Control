int left_val = 0, right_val = 0;

void setup() {
  Serial.begin(9600);
}

void loop(){
  left_val = analogRead(A0);  

  right_val = analogRead(A1);

  Serial.print('L');
  Serial.println(left_val);
  Serial.flush();

  delay(300);
  
  Serial.print('R');
  Serial.println(right_val);
  Serial.flush();

  delay(300);
}
