#このプログラムは、モータドライブ回路が正しく実装できたかどうかをテストするためのプログラムである
#速度はPWMで制御をしておらず、digitalWriteでのONとOFFで行っているため、フルスピードで回転する
#順回転（2秒）→ブレーキ（2秒）→逆回転（2秒）→停止（2秒）を無限に繰り返す
#プログラムを止めるときは、停止もしくはブレーキ中に行う（モータが回転中に止めると、回転しっぱなしになることがある）
#作製するプログラムでは、softPwmで速度をコントロールする必要がある

import time, wiringpi as pi #timeライブラリとwiringpiライブラリ（piとする）を読み込む

#モータドライバの接続ピンを指定する
IN1 = 12 #IN1
IN2 = 16 #IN2
#IN1 IN2 モード
# 0   0  停止
# 1   0  順回転
# 0   1  逆回転
# 1   1  ブレーキ

#初期設定
pi.wiringPiSetupGpio()
pi.pinMode( IN1, 1 )
pi.pinMode( IN2, 1 )

#停止状態にしておく
pi.digitalWrite( IN1, 0 )
pi.digitalWrite( IN2, 0 )

while True:
    #順回転
    pi.digitalWrite( IN1, 1 )
    pi.digitalWrite( IN2, 0 )
    time.sleep(2)
    
    #ブレーキ
    pi.digitalWrite( IN1, 1 )
    pi.digitalWrite( IN2, 1 )
    time.sleep(2)
    
    #逆回転
    pi.digitalWrite( IN1, 0 )
    pi.digitalWrite( IN2, 1 )
    time.sleep(2)
    
    #停止
    pi.digitalWrite( IN1, 0 )
    pi.digitalWrite( IN2, 0 )
    time.sleep(2)


