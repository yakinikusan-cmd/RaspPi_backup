import wiringpi as wp
SW1 =5
LED1 =19
wp.wiringPiSetupGpio()
wp.pinMode(SW1,0)
wp.pinMode(LED1,1)
while True:
    if wp.digitalRead(SW1) == 0:
        #print("x")
        wp.digitalWrite(LED1,1)
    else:
        #print("a")
        wp.digitalWrite(LED1,0)