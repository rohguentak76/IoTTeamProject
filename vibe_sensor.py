import time
import RPi.GPIO as gpio
vibe_pin = 12
gpio.setmode(gpio.BCM)
gpio.setup(vibe_pin, gpio.IN) # gpio for vibe

def vibe_sensor():
	a = gpio.input(vibe_pin)
	if a == 0 :
		print("vibe is sensing")
	else :
		print("nothing")
		
		
while True :
	vibe_sensor()
	time.sleep(2)
