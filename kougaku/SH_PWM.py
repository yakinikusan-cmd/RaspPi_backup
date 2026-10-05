#実験１
#ソフトウェアPWMとハードウェアPWM信号の比較
#LXTeaminalからでないとハードウェアPWMは実行できない
#実行する前に保存すること
#プログラムを停止する場合は，Ctrl+cで止める

import wiringpi as pi #毎回wiringpiと書くのは面倒なので、piとする

SW_PWM_pin = 26 #ソフトウェアPWM信号のGPIOを指定する
HW_PWM_pin = 13 #ハードウェアPWM信号のGPIOを指定する
PWM_RANGE = 1024 #レンジの設定：既定値は1024

Max = int(input('最大値='))
Pwm = int(input('PWM値='))
Clock = int(input('クロック='))
Duty = int(input('比率='))

pi.wiringPiSetupGpio( )
pi.pinMode( SW_PWM_pin, 1 )
pi.softPwmCreate( SW_PWM_pin, 0, Max)

pi.softPwmWrite( SW_PWM_pin, Pwm)

pi.pinMode( HW_PWM_pin, 2 )
pi.pwmSetMode( pi.PWM_MODE_MS )
pi.pwmSetRange( PWM_RANGE )
pi.pwmSetClock( Clock )

pi.pwmWrite( HW_PWM_pin, Duty )

#pythonの実行が終わると信号も停止するので、何もしない処理（pass）を無限に繰り返す
while True :
    pass
