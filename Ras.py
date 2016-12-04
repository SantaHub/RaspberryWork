# turn on LED.
#At raspberry pi
import  RPi.GPIO as gp
import time
gp.setmode(gp.BOARD)
gp.setup(12,gp.OUT) #setsup the given pin for use

while 1:
	gp.output(12,gp.HIGH) #Turn offs the LED
    time.sleep(1)
	gp.output(12,gp.LOW)  #Gives high or low -- high for on and low for off
    time.sleep(1)



# to recieve the input from the ardino to raspberry pi

# AT raspberry pi
import Serial
import RPi.GPIO

scr = serial.Serial('/dev/ttyACM0',9600)

while 1:
	p = scr.read()
	print(p)

# At arduino
 char x; 
void setup(){
	Serial.begin(9600);
}

void loop() {
	digitalWrite('hi');
}

###########################################################

# To recieve data from raspberry pi and glow LED

# At Ardino
char x; 
void setup(){
	
	pinMode(7,OUTPUT);
	Serial.begin(9600);
	digitalWrite(7,LOW);

}

void loop() {
	x= Serial.read();
	if(x=='A')
	 digitalWrite(7,HIGH);
}

# AT Raspberry
import Serial
import RPi.GPIO

scr = serial.Serial('/dev/ttyACM0',9600)

while 1:
	time.sleep(1)
	scr.write('A')