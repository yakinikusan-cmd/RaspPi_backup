import random
import time
import tkinter
import sys
game = 0
count = -1
def game_control(button_num = "null"):
    global game,start_time
    if game == 0:
        start.destroy()
        game = 1
        start_time  = time.time()
        button.place(x = random.randint(30,600),y = random.randint(20,270))
        button1.place(x = random.randint(30,600),y = random.randint(20,270))
    if game == 1:
        if time.time() - start_time < 10:
            move(button_num)
        else:
            game = 2
            button.destroy()
            button1.destroy()
            
    
def move(button_num):
    global count
    if button_num == 0:
        button.place(x = random.randint(30,600),y = random.randint(20,270))
    else:
        button1.place(x = random.randint(30,600),y = random.randint(20,270))
    count += 1
    point.configure(text ="point: " + str(count))
    
    print(count)
root = tkinter.Tk()
root.geometry("640x300")
button = tkinter.Button(root,text = "click me!",command = lambda:game_control(button_num = 0))
button1 = tkinter.Button(root,text = "click me!",command = lambda:game_control(button_num = 1))
start = tkinter.Button(root,text = "start!",command = game_control)
point = tkinter.Label(root,text = str(count))
start.place(x = 320,y = 150)
point.place(x = 40,y = 20)


root.mainloop()







