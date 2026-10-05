import tkinter
import wiringpi as pi
import sys

IN1 = 12 #IN1
IN2 = 16 #IN2
PWM_Max = 100 #最大値は100

def motor_ctrl(mode, speed) :
    if mode == 0 : #停止
        pi.softPwmWrite( IN1, 0)
        pi.softPwmWrite( IN2, 0)

        pass
    elif mode == 1 : #順回転
        pi.softPwmWrite( IN1, speed)
        pi.softPwmWrite( IN2, 0)

        pass
    elif mode == 2 : #逆回転
        pi.softPwmWrite( IN1, 0)
        pi.softPwmWrite( IN2, speed)

        pass
    elif mode == 3 : #ブレーキ
        pi.softPwmWrite( IN1, 100)
        pi.softPwmWrite( IN2, 100)
        pass
    else :
        print('Error')

def changed_value(n=None) :
    motor_state = motor_mode.get() 
    sp = motor_speed.get()
    motor_ctrl(motor_state, sp)

#Main
pi.wiringPiSetupGpio()
pi.pinMode( IN1, 1 )
pi.pinMode( IN2, 1 )
pi.softPwmCreate(IN1,0,PWM_Max)
pi.softPwmCreate(IN2,0,PWM_Max)
pi.softPwmWrite( IN1, 0)
pi.softPwmWrite( IN2, 0)

root=tkinter.Tk()
root.title('モータ制御')

motor_mode = tkinter.IntVar()
motor_mode.set(0)
motor_speed = tkinter.IntVar()
motor_speed.set(0)

label1 = tkinter.Label(root, text = 'モータ制御')
stop = tkinter.Radiobutton(root, text = '停止', variable = motor_mode, value = 0, command = changed_value)
forward = tkinter.Radiobutton(root, text = '順回転', variable = motor_mode, value = 1, command = changed_value)
backward = tkinter.Radiobutton(root, text = '逆回転', variable = motor_mode, value = 2, command = changed_value)
brake = tkinter.Radiobutton(root, text = 'ブレーキ', variable = motor_mode, value = 3, command = changed_value)
scale1 = tkinter.Scale(root, label='速度', orient ='h', from_ = 0, to = PWM_Max, variable = motor_speed, command = changed_value)
button_bye = tkinter.Button(root, text='終了', command = sys.exit)

label1.grid(row=0, column=0, columnspan=4,padx=1, pady=1)
stop.grid(row=1, column=0,padx=1, pady=1)
forward.grid(row=1, column=1,padx=1, pady=1)
backward.grid(row=1, column=2,padx=1, pady=1)
brake.grid(row=1, column=3,padx=1, pady=1)
scale1.grid(row=2, column=0, columnspan=4, sticky='ew', padx=1, pady=1)
button_bye.grid(row=3, column=0, columnspan=4, padx=1, pady=1)
root.mainloop()
