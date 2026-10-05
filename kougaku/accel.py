import mpu6050
import oled
import time
from PIL import ImageFont

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
    draw.text((0,0),"重力加速度[g]",font = ifont,fill = 255)
    draw.text((0,fsize),"x軸:%6.2f"%accel_x,font = ifont,fill = 255)
    draw.text((0,fsize*2),"y軸:%6.2f"%accel_y,font = ifont,fill = 255)
    draw.text((0,fsize*3),"z軸:%6.2f"%accel_z,font = ifont,fill = 255)
    disp.image(image)
    disp.show()
    time.sleep(0.1)
    print(accel_x,accel_y,accel_z)



