const int WINDOW_SIZE = 10; // Кол-во считываемых значений для проверки потенциала

int threshold_val = 300; // Пороговое значение

int left_hand = 0, right_hand = 0;
int left_vals[WINDOW_SIZE], right_vals[WINDOW_SIZE];
int curr_l = 0, curr_r = 0;

int get_array_elem(int arr[WINDOW_SIZE], int (&cmp)(int, int)) {
  int val = arr[0];
  
  for (int i = 1; i < WINDOW_SIZE; i++) {
    if (cmp(arr[i], val))
      val = arr[i];  
  }

  return val;
}

int cmp_min(int l, int r) {
  return l < r;
}

int cmp_max(int l, int r) {
  return l > r;
}

int check_potential(int arr[WINDOW_SIZE]) {
 int min_val = get_array_elem(arr, cmp_min);
 int max_val = get_array_elem(arr, cmp_max);

 return max_val - min_val > threshold_val;
}

void setup() {
  Serial.begin(9600);
}

void loop(){
  left_hand = analogRead(A0);
  right_hand = analogRead(A1);

  if (curr_l < WINDOW_SIZE) {
    left_vals[curr_l++] = left_hand;
  }
  else {
    left_hand = check_potential(left_vals);   
    curr_l = 0;   
  }

  if (curr_r < WINDOW_SIZE) {
    right_vals[curr_r++] = right_hand;
  }
  else {
    right_hand = check_potential(right_vals); 
    curr_r = 0; 
  }

  Serial.print('L');
  Serial.println(left_hand);
  Serial.flush();

  delay(300);
  
  Serial.print('R');
  Serial.println(right_hand);
  Serial.flush();


  delay(300);
}
