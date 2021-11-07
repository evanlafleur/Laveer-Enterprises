//Declaration of Variables
const int redA = 2;
const int redB = 3;
const int blueA = 4;
const int blueB = 5;
const int whiteA = 6;
const int whiteB = 7;
const int purpleA = 8;
const int purpleB = 9;
const int greenA = 10;
const int greenB = 11;
int incomingByte;




void setup() {
  Serial.begin(9600);
  pinMode (redA, OUTPUT);
  pinMode (redB, OUTPUT);
  pinMode (blueA, OUTPUT);
  pinMode (blueB, OUTPUT);
  pinMode (whiteA, OUTPUT);
  pinMode (whiteB, OUTPUT);
  pinMode (purpleA, OUTPUT);
  pinMode (purpleB, OUTPUT);
  pinMode (greenA, OUTPUT);
  pinMode (greenB, OUTPUT);

}

//Declares different Name for Motor Pins
void PinOn(int pin){
  digitalWrite(pin, HIGH);
  }
void PinOff(int pin){
  digitalWrite(pin, LOW);
  }
void serialFlush(){
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
} 

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'U'){
      Serial.println("Going Up");
      up();
      if (incomingByte == 'H'){}
        halt();
      }
    if (incomingByte == 'D'){
      Serial.println("Going Down");
      down();
      serialFlush();
      }
    if (incomingByte == 'L'){
      Serial.println("Strafe Left");
      sleft();
      serialFlush();
      }
    if (incomingByte == 'R'){
      Serial.println("Strafe Right");
      sright();
      serialFlush();
      } 
    if (incomingByte == 'Y'){
      Serial.println("Rotate Right");
      rrotate();
      serialFlush();
      }  
    if (incomingByte == 'T'){
      Serial.println("Rotate Left");
      lrotate();
      serialFlush();
      }  
    if (incomingByte == 'F'){
      Serial.println("Going Forward");
      forward();
      serialFlush();
      }  
    if (incomingByte == 'B'){
      Serial.println("Going Backward");
      backward();
      serialFlush();
      }  
    if (incomingByte == 'P'){
      tup();
      serialFlush();
      }  
    if (incomingByte == 'O'){
      tdown();
      serialFlush();
      }   
    }
}

void forward(){
  PinOn(redA);
  PinOff(redB);
  PinOn(blueA);
  PinOff(blueB);
  Serial.println("Tipping Forward");
  }

void backward(){
  PinOff(redA);
  PinOn(redB);
  PinOff(blueA);
  PinOn(blueB);
  Serial.println("Tipping Backward");
  }

void up(){
  PinOff(whiteA);
  PinOn(whiteB);
  PinOff(purpleA);
  PinOn(purpleB);
  }
void down(){
  PinOn(whiteA);
  PinOff(whiteB);
  PinOn(purpleA);
  PinOff(purpleB);
  }
void sleft(){
  PinOff(greenA);
  PinOn(greenB);
  }
void sright(){
  PinOn(greenA);
  PinOff(greenB);
  }
void rrotate(){
  PinOn(redA);
  PinOff(redB);
  PinOff(blueA);
  PinOn(blueB);
  }

void lrotate(){
  PinOff(redA);
  PinOn(redB);
  PinOn(blueA);
  PinOff(blueB);
  }
void tup(){
  PinOn(whiteA);
  PinOff(whiteB);
  PinOff(purpleA);
  PinOn(purpleB);
  }
void tdown(){
  PinOff(whiteA);
  PinOn(whiteB);
  PinOn(purpleA);
  PinOff(purpleB);
  }
void halt(){
  PinOff(whiteA);
  PinOff(whiteB);
  PinOff(purpleA);
  PinOff(purpleB);
  PinOff(redA);
  PinOff(redB);
  PinOff(blueA);
  PinOff(blueB);
  PinOff(greenA);
  PinOff(greenB);
  }

