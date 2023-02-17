//---------------------------------//
// Sensor Array Functions 
//    Used to calculate the distance of the sensors from the walls 
//    along with update the sensor array global variable to be used in navagation
//---------------------------------//

// defines pins numbers 
//****ADD MORE PINS IF THERE ARE MORE SENSORS******//
  const int trigPin1 = 13, echoPin1 = 12;
  const int trigPin2 = 11, echoPin2 = 10;

// Sets up the sensor array with the given constants
//****ADD AN ARRAY FOR EACH SENSOR FORMAT: { distance, trigPin, EchoPin}******//
int sensorArray[2][3] = {{0, trigPin1, echoPin1}, {0, trigPin2, echoPin2}};

// Correctly Sets the Initial state of Sensor pinouts for all sensors
void sensorArraySetup(){
  Serial.println("---------Sensor Setup---------");
  // Calculating number of sensors
  int sensorArraySize = sizeof(sensorArray)/sizeof(sensorArray[0]);
  for (int i = 0; i < sensorArraySize; i++){
    int trig = sensorArray[i][1];
    int echo = sensorArray[i][2];
    pinMode(trig, OUTPUT); // Sets the trigPin as an Output
    pinMode(echo, INPUT); // Sets the echoPin as an Input
    Serial.print("Sensor: "); Serial.print(i); Serial.print(" Set with Trig Pin: "); 
    Serial.print(trig); Serial.print(" Echo pin: "); Serial.println(echo);
  }
}

// Updates each sensor's distance in the sensor array
void updateSensors(){
  Serial.println("---------Sensor Update---------");
  // Calculating number of sensors
  int sensorArraySize = sizeof(sensorArray)/sizeof(sensorArray[0]);
  for (int i = 0; i < sensorArraySize; i++){
    // Array traversal
      int duration, distance;
      int trig = sensorArray[i][1];
      int echo = sensorArray[i][2];

    // Sending signals to gather data
      digitalWrite(trig, LOW);
      delayMicroseconds(2);
      digitalWrite(trig, HIGH);
      delayMicroseconds(10);
      digitalWrite(trig, LOW);
      duration = pulseIn(echo, HIGH);

    // Added historisa to cutdown on jitter
      distance = duration * 0.034 / 2;    
      sensorArray[i][0] = distance;

    // Printing calculations  
      Serial.print("Sensor: "); Serial.print(i);
      Serial.print(" found the distance to be: "); Serial.println(distance);
  }
}

//---------------------------------//
// Micro Mouse 2023 Setup & Loop
//---------------------------------//
void setup() {
  Serial.begin(9600); // Starts the serial communication
  Serial.println();   // Just for better formed output
  sensorArraySetup(); // Turns on the sensors in the sensor array
}
void loop() {
  delayMicroseconds(9000);
  updateSensors();    // Updates distance measured by each sensor
}