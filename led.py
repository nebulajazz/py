from gpio import *
from time import *

pinMode(1,OUTPUT)
i=0
while i<5:
	digitalWrite(1,HIGH)
	delay(1000)
	digitalWrite(1,LOW)
	delay(1000)
	print(i)
	i=i+1
