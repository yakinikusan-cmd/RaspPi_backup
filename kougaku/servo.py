import sg90
import wiringpi
import time

wiringpi.wiringPiSetupGpio( )

# サーボモータに接続したGPIO端子番号を指定
servo_pin = 13
servo2 =12
# サーボモータを動かす角度を指定する
while True:
    sg90.sg90_set(servo_pin, 0)
    sg90.sg90_set(servo2, 0)
    time.sleep(1)
    sg90.sg90_set(servo_pin, 90)
    time.sleep(1)
    sg90.sg90_set(servo_pin, -90)
    time.sleep(1)