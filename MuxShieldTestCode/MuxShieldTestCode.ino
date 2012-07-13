//Mux_Shield_AnalogIn_Example
//http://mayhewlabs.com/arduino-mux-shield

/*
This example shows how to read and store all 48 pins as analog inputs into arrays and print the results over serial.
Multiplexer pin inputs that do not have a voltage reading (i.e nothing connected) will have erratic values.

To simplify this code further, one might use nested for loops or function calls.
*/

//Give convenient names to the control pins
#define CONTROL0 5    
#define CONTROL1 4
#define CONTROL2 3
#define CONTROL3 2

//Create arrays for data from the the MUXs
//See the Arduino Array Reference: http://www.arduino.cc/en/Reference/Array
int mux0array[16];
int mux1array[16];
int mux2array[16];

void setup()
{
  //Set MUX control pins to output
  pinMode(CONTROL0, OUTPUT);
  pinMode(CONTROL1, OUTPUT);
  pinMode(CONTROL2, OUTPUT);
  pinMode(CONTROL3, OUTPUT);
  
  //Open the serial port at 28800 bps
  Serial.begin(28800);
}
  

void loop()
{
  //This for loop is used to scroll through and store the 16 inputs on the FIRST multiplexer
  for (int i=0; i<16; i++)
  {
    //The following 4 commands set the correct logic for the control pins to select the desired input
    //See the Arduino Bitwise AND Reference: http://www.arduino.cc/en/Reference/BitwiseAnd
    //See the Aruino Bitshift Reference: http://www.arduino.cc/en/Reference/Bitshift
    digitalWrite(CONTROL0, (i&15)>>3); 
    digitalWrite(CONTROL1, (i&7)>>2);  
    digitalWrite(CONTROL2, (i&3)>>1);  
    digitalWrite(CONTROL3, (i&1));     
    
    //Read and store the input value at a location in the array
    mux0array[i] = analogRead(0);
  }
  
  //This for loop is used to scroll through the SECOND multiplexer
  for (int i=0; i<16; i++)
  {
    digitalWrite(CONTROL0, (i&15)>>3); 
    digitalWrite(CONTROL1, (i&7)>>2);  
    digitalWrite(CONTROL2, (i&3)>>1);  
    digitalWrite(CONTROL3, (i&1));     
    mux1array[i] = analogRead(1);
  }
  
  //This for loop is used to scroll through the THIRD multiplexer
  for (int i=0; i<16; i++)
  {
    digitalWrite(CONTROL0, (i&15)>>3); 
    digitalWrite(CONTROL1, (i&7)>>2);  
    digitalWrite(CONTROL2, (i&3)>>1);  
    digitalWrite(CONTROL3, (i&1));     
    mux2array[i] = analogRead(2);
  }    
  
  //The following lines are for printing out results of array0
  Serial.print("mux0array: ");
  for (int i=0; i<16; i++)
  {
    Serial.print(mux0array[i]);
    Serial.print("-");
  }
  Serial.println();  //line feed
  
  //The following lines are for printing out results of array1
  Serial.print("mux1array: ");
  for (int i=0; i<16; i++)
  {
    Serial.print(mux1array[i]);
    Serial.print("-");
  }
  Serial.println();
  
  //The following lines are for printing out results of array2
  Serial.print("mux2array: ");
  for (int i=0; i<16; i++)
  {
    Serial.print(mux2array[i]);
    Serial.print("-");
  }
  Serial.println();
  
}
