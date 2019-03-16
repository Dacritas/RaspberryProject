import RPi.GPIO as GPIO # Import GPIO library

GPIO.setmode(GPIO.BOARD) #Use GPIO pin numbering
GPIO.setup(7, GPIO.OUT) #Setup GPIO Pin 7 to Out 
GPIO.output(7, True) #Turn on GPIO pin 7