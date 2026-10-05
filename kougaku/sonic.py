import hcsr04
import wiringpi as wp
import oled
import time
from PIL import ImageFont

disp,image,draw=oled.oled_setup()
fsize = 16
ifont = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', fsize, encoding = 'unic')
wp.wiringPiSetupGpio()

while True:
    d = hcsr04.distance()
    draw.text((0,0),str(round(d,3))+"cm",font = ifont,fill = 255)
    disp.image(image)
    disp.show()
    time.sleep(0.1)
    oled.oled_clear(draw)
    

