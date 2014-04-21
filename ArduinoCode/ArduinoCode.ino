#include <PWMServo.h>

/*
Directly control a servo.
 */
#include <stdlib.h>


#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>


SoftwareSerial mySerial(8, 7);

Adafruit_GPS GPS(&mySerial);


PWMServo servo1;

// this keeps track of whether we're using the interrupt
// off by default!
boolean usingInterrupt = false;
//void useInterrupt(boolean); // Func prototype keeps Arduino 0023 happy

// Set GPSECHO to 'false' to turn off echoing the GPS data to the Serial console
// Set to 'true' if you want to debug and listen to the raw GPS sentences. 
#define GPSECHO  false

#define DEBUG false

//Servo servo2;

void setup() 
{
  Serial.begin(115200);


 // 9600 NMEA is the default baud rate for Adafruit MTK GPS's- some use 4800
  GPS.begin(9600);
  if(DEBUG){
    Serial.println("Adafruit GPS library basic test!");
  }
  
  // uncomment this line to turn on RMC (recommended minimum) and GGA (fix data) including altitude
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  // uncomment this line to turn on only the "minimum recommended" data
  //GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCONLY);
  // For parsing data, we don't suggest using anything but either RMC only or RMC+GGA since
  // the parser doesn't care about other sentences at this time

  // Set the update rate
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);   // 1 Hz update rate
  // For the parsing code to work nicely and have time to sort thru the data, and
  // print it out we don't suggest using anything higher than 1 Hz
  
  // Request updates on antenna status, comment out to keep quiet
  GPS.sendCommand(PGCMD_ANTENNA);
  
  // the nice thing about this code is you can have a timer0 interrupt go off
  // every 1 millisecond, and read data from the GPS for you. that makes the
  // loop code a heck of a lot easier!
  useInterrupt(false);
  

  servo1.attach(9); // Attach to servo in pin 5
//  servo2.attach(6); // Attach to servo in pin 6
  servo1.write(90); // Set it dead on. 
//  servo2.write(180); //Just so I know who's who
  while (! Serial); // Wait untilSerial is ready - Leonardo
  
  if(DEBUG){
    Serial.println("Enter Degree between 0 and 180");
  }
  
  delay(1000);
  // Ask for firmware version
  mySerial.println(PMTK_Q_RELEASE);
}


void useInterrupt(boolean v) {
  if (v) {
    // Timer0 is already used for millis() - we'll just interrupt somewhere
    // in the middle and call the "Compare A" function above
    OCR0A = 0xAF;
    TIMSK0 |= _BV(OCIE0A);
    usingInterrupt = true;
  } else {
    // do not call the interrupt function COMPA anymore
    TIMSK0 &= ~_BV(OCIE0A);
    usingInterrupt = false;
  }
}

uint32_t timer = millis();
void loop() 
{
// Serial.println("InLoop");

  // in case you are not using the interrupt above, you'll
  // need to 'hand query' the GPS, not suggested :(
  if (! usingInterrupt) {
    // read data from the GPS in the 'main loop'
    char c = GPS.read();
    // if you want to debug, this is a good time to do it!
    if (GPSECHO)
      if (c) Serial.print(c);
  }
  
  // if a sentence is received, we can check the checksum, parse it...
  if (GPS.newNMEAreceived()) {
    // a tricky thing here is if we print the NMEA sentence, or data
    // we end up not listening and catching other sentences! 
    // so be very wary if using OUTPUT_ALLDATA and trytng to print out data
    //Serial.println(GPS.lastNMEA());   // this also sets the newNMEAreceived() flag to false
  
    if (!GPS.parse(GPS.lastNMEA()))   // this also sets the newNMEAreceived() flag to false
      return;  // we can fail to parse a sentence in which case we should just wait for another
  }
  
  if (Serial.available())
  {
  // if millis() or timer wraps around, we'll just reset it
  // if (timer > millis())  timer = millis();
  
      int inOption = Serial.read();
      int angle = 0;
      
      if(inOption == 'A'){
        servo1.write(ReadNumbers());
        delay(15); // Wait for the servo to get there.
      }
      
      else if (inOption == 'B'){
        Serial.println((int)GPS.fix);
        ReadNumbers();
      }
      
      else if( inOption == 'C'){
        getLocation();
        ReadNumbers();
      }
      else{
        Serial.println("Invalid Option: ");
      }
  }
  
  if (DEBUG){
    // if millis() or timer wraps around, we'll just reset it
  if (timer > millis())  timer = millis();

  // approximately every 2 seconds or so, print out the current stats
  if (millis() - timer > 2000) { 
    timer = millis(); // reset the timer
    
    Serial.print("\nTime: ");
    Serial.print(GPS.hour, DEC); Serial.print(':');
    Serial.print(GPS.minute, DEC); Serial.print(':');
    Serial.print(GPS.seconds, DEC); Serial.print('.');
    Serial.println(GPS.milliseconds);
    Serial.print("Date: ");
    Serial.print(GPS.day, DEC); Serial.print('/');
    Serial.print(GPS.month, DEC); Serial.print("/20");
    Serial.println(GPS.year, DEC);
    Serial.print("Fix: "); Serial.print((int)GPS.fix);
    Serial.print(" quality: "); Serial.println((int)GPS.fixquality); 
    if (GPS.fix) {
      Serial.print("Location: ");
      Serial.print(GPS.latitude, 4); Serial.print(GPS.lat);
      Serial.print(", "); 
      Serial.print(GPS.longitude, 4); Serial.println(GPS.lon);
      
      Serial.print("Speed (knots): "); Serial.println(GPS.speed);
      Serial.print("Angle: "); Serial.println(GPS.angle);
      Serial.print("Altitude: "); Serial.println(GPS.altitude);
      Serial.print("Satellites: "); Serial.println((int)GPS.satellites);
    }
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

int getLocation()
{
  if (GPS.fix) {

    // South is negative
    if(GPS.lat == 'S')
    {
      Serial.print("-");
    }
    Serial.print(GPS.latitude, 4);   
    Serial.print(","); 
    
    // West is negative
    if(GPS.lon == 'W')
    {
      Serial.print("-");
    }    
    Serial.print(GPS.longitude, 4);
    Serial.println();
  }
  else{
   Serial.println("FALSE"); 
  }
}
