import oled
import time
from PIL import ImageFont
disp,image,draw=oled.oled_setup()
fsize = 16
ifont = ImageFont.truetype('/usr/share/fonts/oled/Shinonome/Shinonome16.ttf', fsize, encoding = 'unic')
while True:
    draw.text((0,0),"只今の日時は",font = ifont,fill = 255)
    draw.text((0,fsize),time.strftime("%Y年%m月%d日",time.localtime()),font = ifont,fill = 255)
    draw.text((0,fsize*2),time.strftime("%H時%M分%S秒",time.localtime()),font = ifont,fill = 255)
    draw.text((0,fsize*3),"です。",font = ifont,fill = 255)
    disp.image(image)
    disp.show()
    time.sleep(0.1)
    oled.oled_clear(draw)
