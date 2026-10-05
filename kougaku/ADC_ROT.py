import sg90
import wiringpi
import mcp3208
import time


wiringpi.wiringPiSetupGpio()
CE = 0 #SPIデバイスの指定
SPEED = 1000000 #通信速度Hz（1MHzを指定．1秒間に100万bitを転送）
Vref = 3.307 #基準電圧（Raspberry Piの3.3V端子の電圧を測定し，その値を記入する）
CH = 0 #アナログ入力チャンネルの指定

mcp3208.Setup(CE, SPEED)

# サーボモータに接続したGPIO端子番号を指定
servo_pin = 13
# サーボモータを動かす角度を指定する
while True:
    data, volt = mcp3208.ReadData(CE, CH, Vref)
    angle = data/4095*180-90
    sg90.sg90_set(servo_pin, angle)
    time.sleep(0.01)
