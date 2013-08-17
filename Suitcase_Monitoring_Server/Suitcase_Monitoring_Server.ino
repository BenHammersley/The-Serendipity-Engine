/*
  Web Server
 
 A simple web server that shows the value of the analog input pins.
 using an Arduino Wiznet Ethernet shield. 
 
 Circuit:
 * Ethernet shield attached to pins 10, 11, 12, 13
 * Analog inputs attached to pins A0 through A5 (optional)
 
 created 18 Dec 2009
 by David A. Mellis
 modified 9 Apr 2012
 by Tom Igoe
 
 */

#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = { 
  0x90, 0xA2, 0xDA, 0x0D, 0xA7, 0xB9 };
IPAddress ip(192,168,0,177);
IPAddress gateway(192,168,0,1);
IPAddress subnet(255,255,255,0);

// Initialize the Ethernet server library
// with the IP address and port you want to use 
// (port 80 is default for HTTP):
EthernetServer server(80);

void setup() {
 // Open serial communications and wait for port to open:
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
}


void loop() {
  // listen for incoming clients
  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          // send a standard http response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
	  client.println("Refresh: 1");  // refresh the page automatically every 5 sec
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          client.println("<h1>Serendipity Engine Suitcase Debug Page</h1>");
          client.println("<p>The ethernet shield has the IP Address: ");
          client.println(Ethernet.localIP());
          
          client.println("<h2>Analog Inputs</h2>");

          // output the value of each analog input pin
          for (int analogChannel = 0; analogChannel < 4; analogChannel++) {
            // delay a little to let the sensors settle
            delay(10);
            int sensorReading = analogRead(analogChannel);
            client.print("Analog Input ");
            client.print(analogChannel);
            client.print(" is ");
            if (sensorReading > 500)
              {
                client.println("<font color='red'><b> OFF </b></font>");
              }
            
            if (sensorReading < 500)
              {
                client.println("<font color='green'><b> ON </b></font>");
              }  
            
            client.print("         Sensor value= ");
            client.print(sensorReading);
  
            client.println("<br/>");       
          }
          
          
          client.println("<h2>Prose Output</h2><p>");
          
          if (analogRead(0) > 500) 
          { 
            client.println("You think you can get the best chocolate in France,");
          }
          
          if (analogRead(0) < 500) 
          { 
            client.println("You think you can get the best chocolate in Spain,");
          }
  
            if (analogRead(1) > 500) 
          { 
            client.println("but you woke on the wrong side of the bed. Oh no!");
          }
          
          if (analogRead(1) < 500) 
          { 
            client.println("and you have been rewarded with bountiful sleep.");
          }
          
          client.println("<br/>");
                  
          if (analogRead(2) > 500) 
          { 
            client.println("You may have the jitters. Try to relax.");
          }
          
          if (analogRead(2) < 500) 
          { 
            client.println("More of a tea person, huh?");
          }
           
         
           if (analogRead(3) > 500) 
          { 
            client.println("You inspire with your optimism.");
          }
          
          if (analogRead(3) < 500) 
          { 
            client.println("You are strong, and never give up.");
          }
          
   
          client.println("</p>");                        
          
          
          client.println("<h2>Digital Inputs (Currently Unused)</h2>");

            // output the value of each analog input pin
          for (int digitalChannel = 2; digitalChannel < 8; digitalChannel++) {
            int sensorReading = digitalRead(digitalChannel);
            client.print("Digital Input ");
            client.print(digitalChannel);
            client.print(" is ");
            client.print(sensorReading);
            client.println("<br />");       
          }
          
          client.println("</html>");
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } 
        else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
    Serial.println("client disonnected");
  }
}

