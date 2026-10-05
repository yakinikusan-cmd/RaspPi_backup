import tkinter
import wiringpi as wp
import sys
import sg90


def value_changed(n=None) : 
    #print(servo_state.get())
    if servo_state.get():
        sg90.sg90_set(SERVO_PIN, angle.get())

    else:
        sg90.sg90_set(SERVO_PIN, 0)

 
root=tkinter.Tk() 
root.title('サーボモータ制御')

servo_state = tkinter.IntVar() 
servo_state.set(0) 
angle = tkinter.IntVar()
angle.set(0)

label1 = tkinter.Label(root, text = 'サーボモータ制御')

rbutton_off = tkinter.Radiobutton(root, text = 'OFF',variable = servo_state,value=0, command = value_changed)
rbutton_on  = tkinter.Radiobutton(root, text = 'ON',variable = servo_state,value=1, command = value_changed)

scale1 = tkinter.Scale(root, label='角度', orient ='h', from_ = -90, to = 90,variable = angle,command = value_changed)


button_exit = tkinter.Button(root, text='終了', command = sys.exit)

SERVO_PIN = 13

wp.wiringPiSetupGpio()


label1.grid(row=0, column=0, columnspan=2,padx=1, pady=1)
rbutton_off.grid(row=1, column=0,padx=1, pady=1)
rbutton_on.grid( row=1, column=1,padx=1, pady=1)
scale1.grid(row=2, column=0,columnspan = 2,padx=1, pady=1)
button_exit.grid(row=3, column=0,columnspan = 2,padx=1, pady=1)

#メインループ
root.mainloop()




