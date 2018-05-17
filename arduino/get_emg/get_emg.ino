const int WINDOW_SIZE = 10; // Кол-во считываемых значений для проверки потенциала

int count_to_setup = 3; // Кол-во сжиманий рук для настройки программы
int min_threshold_val = 200; // Минимально пороговое значение
int threshold_val = -1; // Пороговое значение

int left_hand = 0, right_hand = 0; // Значения на левой и правой руках
int left_vals[WINDOW_SIZE], right_vals[WINDOW_SIZE]; // Массив значений на левой и правой руках
int curr_l = 0, curr_r = 0; // Номер текущего считанного значения

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

void setup_threshold(int arr[WINDOW_SIZE]) {
  int min_val = get_array_elem(arr, cmp_min);
  int max_val = get_array_elem(arr, cmp_max);

  if (max_val - min_val > min_threshold_val) {
    threshold_val = threshold_val == -1 ? max_val - min_val : (threshold_val + max_val - min_val) / 2;
    count_to_setup--;
  }
}

int check_potential(int arr[WINDOW_SIZE], int cmp_number) {
 int min_val = get_array_elem(arr, cmp_min);
 int max_val = get_array_elem(arr, cmp_max);

 return max_val - min_val > cmp_number;
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
    if (count_to_setup > 0) {
      setup_threshold(left_vals);
    }
    else {
      left_hand = check_potential(left_vals, threshold_val);
    }   
    
    curr_l = 0;   
  }

  if (curr_r < WINDOW_SIZE) {
    right_vals[curr_r++] = right_hand;
  }
  else {
    if (count_to_setup > 0) {
      setup_threshold(right_vals);
    }
    else {
      right_hand = check_potential(right_vals, threshold_val);
    }
    
    curr_r = 0; 
  }

  if (count_to_setup > 0) {
    Serial.print('S');
    Serial.println(count_to_setup);
  }
  else {
    if (curr_l == 0) {
      Serial.print('L');
      Serial.println(left_hand);
      Serial.flush();
    }

    if (curr_r == 0) {
      Serial.print('R');
      Serial.println(right_hand);
      Serial.flush();  
    }
  }

  delay(200);
}
