import tkinter
import wiringpi as wp
import sys


def value_changed(n=None) : 
    #print(n)
    st = led_state.get()
    br = brightness.get()
    if st :
        wp.softPwmWrite( PWM_PIN, int(br/100*MAX))
    elif st == 0 :
        wp.softPwmWrite( PWM_PIN, 0)

root=tkinter.Tk() 
root.title('LED制御')

led_state = tkinter.IntVar() 
led_state.set(0) 
brightness = tkinter.IntVar()
brightness.set(0)

label1 = tkinter.Label(root, text = 'LEDスイッチ')

rbutton_off = tkinter.Radiobutton(root, text = 'OFF',variable = led_state,value=0, command = value_changed)
rbutton_on  = tkinter.Radiobutton(root, text = 'ON',variable = led_state,value=1, command = value_changed)

scale1 = tkinter.Scale(root, label='明るさ', orient ='h', from_ = 0, to = 100,variable = brightness,command = value_changed)


button_exit = tkinter.Button(root, text='終了', command = sys.exit)

PWM_PIN = 19
MAX = 100

wp.wiringPiSetupGpio()
wp.pinMode( PWM_PIN, 1 )
wp.softPwmCreate(PWM_PIN, 0, MAX)
wp.softPwmWrite( PWM_PIN, 0)

label1.grid(row=0, column=0, columnspan=2,padx=1, pady=1)
rbutton_off.grid(row=1, column=0,padx=1, pady=1)
rbutton_on.grid( row=1, column=1,padx=1, pady=1)
scale1.grid(row=2, column=0,columnspan = 2,padx=1, pady=1)
button_exit.grid(row=3, column=0,columnspan = 2,padx=1, pady=1)

#メインループ
root.mainloop()

