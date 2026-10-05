import bme280
import mpu6050
import oled
import time
from PIL import ImageFont
import wiringpi as wp




disp,image,draw=oled.oled_setup()
fsize = 16
ifont = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', fsize, encoding = 'unic')
bme280.bme280_setup()
draw.text((0,fsize*3),"キャリブレーション中…",font = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', 10, encoding = 'unic'),fill = 255)
disp.image(image)
disp.show()
m = mpu6050.mpu6050_setup(1)


while True:
    oled.oled_clear(draw)
    temp,humid,pressure = bme280.get_data_bme280()
    accel_x,accel_y,accel_z = m.readAccelData()
    print(accel_x)
    if (accel_x >0.8) and (accel_x <1.2):
        draw.text((0,0),"只今の日時は",font = ifont,fill = 255)
        draw.text((0,fsize),time.strftime("%Y年%m月%d日",time.localtime()),font = ifont,fill = 255)
        draw.text((0,fsize*2),time.strftime("%H時%M分%S秒",time.localtime()),font = ifont,fill = 255)
        draw.text((0,fsize*3),"です。",font = ifont,fill = 255)
    else:
        draw.text((0,0),"現在の環境情報",font = ifont,fill = 255)
        draw.text((0,fsize),"気温:%7.2f℃"%temp,font = ifont,fill = 255)
        draw.text((0,fsize*2),"湿度:%7.2f％"%humid,font = ifont,fill = 255)
        draw.text((0,fsize*3),"気圧:%7.2fhPa"%(pressure/100),font = ifont,fill = 255)
    disp.image(image)
    disp.show()
    time.sleep(0.1)
# import mpu6050
# import oled
# import time
# from PIL import ImageFont

# disp,image,draw=oled.oled_setup()
# fsize = 16
# ifont = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', fsize, encoding = 'unic')
# draw.text((0,fsize*3),"キャリブレーション中…",font = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', 10, encoding = 'unic'),fill = 255)
# disp.image(image)
# disp.show()
# m = mpu6050.mpu6050_setup(1)


# while True:
#     oled.oled_clear(draw)
#     accel_x,accel_y,accel_z = m.readAccelData()
#     draw.text((0,0),"重力加速度[g]",font = ifont,fill = 255)
#     draw.text((0,fsize),"x軸:%6.2f"%accel_x,font = ifont,fill = 255)
#     draw.text((0,fsize*2),"y軸:%6.2f"%accel_y,font = ifont,fill = 255)
#     draw.text((0,fsize*3),"z軸:%6.2f"%accel_z,font = ifont,fill = 255)
#     disp.image(image)
#     disp.show()
#     time.sleep(0.1)
# import oled
# import time
# from PIL import ImageFont
# disp,image,draw=oled.oled_setup()
# fsize = 16
# ifont = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', fsize, encoding = 'unic')
# while True:
#     draw.text((0,0),"只今の日時は",font = ifont,fill = 255)
#     draw.text((0,fsize),time.strftime("%Y年%m月%d日",time.localtime()),font = ifont,fill = 255)
#     draw.text((0,fsize*2),time.strftime("%H時%M分%S秒",time.localtime()),font = ifont,fill = 255)
#     draw.text((0,fsize*3),"です。",font = ifont,fill = 255)
#     disp.image(image)
#     disp.show()
#     time.sleep(0.1)
#     oled.oled_clear(draw)



