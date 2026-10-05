import bme280
import oled
import time
from PIL import ImageFont


disp,image,draw=oled.oled_setup()
fsize = 16
ifont = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', fsize, encoding = 'unic')
bme280.bme280_setup()


while True:
    oled.oled_clear(draw)
    temp,humid,pressure = bme280.get_data_bme280()
    draw.text((0,0),"現在の環境情報",font = ifont,fill = 255)
    draw.text((0,fsize),"気温:%7.2f℃"%temp,font = ifont,fill = 255)
    draw.text((0,fsize*2),"湿度:%7.2f％"%humid,font = ifont,fill = 255)
    draw.text((0,fsize*3),"気圧:%7.2fhPa"%(pressure/100),font = ifont,fill = 255)
    disp.image(image)
    disp.show()
    time.sleep(0.1)



