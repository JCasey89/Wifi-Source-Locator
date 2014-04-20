/*
Directly control a servo.
 */
#include <Servo.h>
#include <stdlib.h>


Servo servo1;
//Servo servo2;

void setup() 
{
  Serial.begin(9600);
  servo1.attach(5); // Attach to servo in pin 5
//  servo2.attach(6); // Attach to servo in pin 6
  servo1.write(90); // Set it dead on. 
  servo2.write(180); //Just so I know who's who
  while (! Serial); // Wait untilSerial is ready - Leonardo
  Serial.println("Enter Degree between 0 and 180");
}

void loop() 
{
  if (Serial.available())
  {
      int inOption = Serial.read();
      int angle = 0;
      
      if(inOption == 'A'){
       
        servo1.write(ReadNumbers());
      }
      else if (inOption == 'B'){
//        servo2.write(ReadNumbers());
      }
      else{
        Serial.print("Invalid Option: ");
      }
  }
}

int ReadNumbers(){
  String inString = "";
  int angle;
  int inChar;
  while(inChar = Serial.read()){
  //  int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char 
      // and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string,
    // then the string's value:
    if (inChar == '\n') {
  /*    Serial.print("Value:");
      Serial.println(inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);
      // Return the string for new input: */
      angle =  inString.toInt();
     /* servo1.write(angle);
      Serial.print("Moved to degree: ");
      Serial.println(angle); */
      inString = "";
      break;
    }
  }
  return angle;
}

