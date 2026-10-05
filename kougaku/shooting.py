import mpu6050
import oled
import time
from PIL import ImageFont
import wiringpi as wp
import random
SW1 =5

wp.wiringPiSetupGpio()
wp.pinMode(SW1,0)
ballx = 0
bally = 0
ball = 0
enex = 0
eney = 0
ene = 0
disp,image,draw=oled.oled_setup()
fsize = 16
ifont = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', fsize, encoding = 'unic')
draw.text((0,fsize*3),"キャリブレーション中…",font = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', 10, encoding = 'unic'),fill = 255)
disp.image(image)
disp.show()
m = mpu6050.mpu6050_setup(1)


while True:
    oled.oled_clear(draw)
    accel_x,accel_y,accel_z = m.readAccelData()
    if ball == 0:
        if wp.digitalRead(SW1) == 0:
            ball = 1
            ballx = 110*accel_y
            bally = 40
            draw.ellipse((ballx,bally,ballx+5,bally+5), fill=255)
    else:
        if bally ==  0:
            ball = 0
        bally -= 10
        draw.ellipse((ballx,bally,ballx+5,bally+5), fill=255)
        
    if ene == 0: 
        ene = 1
        enex = random.randint(10,100)
        eney = 0
        draw.pieslice((enex, eney, enex+10, eney+10), start=240, end=300, fill=255)
    else:
        if eney ==  100:
            ene = 0
        eney += 5
        draw.pieslice((enex, eney, enex+20, eney+20), start=240, end=300, fill=255)
    

    draw.ellipse((110*accel_y,55,110*accel_y+10,65), fill=255)
    disp.image(image)
    disp.show()
    time.sleep(0.1)



