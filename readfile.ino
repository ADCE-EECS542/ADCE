
#include <SPI.h>
#include <SD.h>
 

File myFile;
 
void setup() 
{
    Serial.begin(9600);
    while (!Serial) 
    {
    ; // wait for serial port to connect. Needed for native USB port only
      
    }
    
    Serial.print("Initializing SD card...");
 
 
    if (!SD.begin(4)) {
      Serial.println("initialization failed!");
      return;
    }
    Serial.println("initialization done.");
 
    myFile = SD.open("LINGSH~1.TXT");
    if (myFile) {
      Serial.println("LingShunLAB.txt:");
      Serial.println("↓↓↓↓");
      // read from the file until there's nothing else in it:
   
      while (myFile.available()) {
        Serial.write(myFile.read());
      }
      // close the file:

      myFile.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
  }
}
 
void loop() {
  
 
}
