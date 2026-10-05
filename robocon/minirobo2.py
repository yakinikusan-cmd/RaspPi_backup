# -*- coding: utf-8 -*-
"""
KRS_Python_Sample_1
KONDO KAGAKU CO.,LTD.
2021/12/20
"""

import serial
import time
import pygame
import math
import krs_servo

krs = serial.Serial('/dev/ttyUSB0', baudrate=115200, parity=serial.PARITY_EVEN, timeout=0.5)
#サーボのIDを読み出します
bl, reData = krs_servo.krs_getID_CMD(krs)
print("ID", reData)
pygame.init()
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()
print(joy.get_numaxes())
R_Wheel_ID = 0
L_Wheel_ID = 19
measure_ID = 1
while True:
    pygame.event.pump()
#     # x_data = joy.get_axis(0)
#     # y_data = joy.get_axis(1)
#     # theta_data = joy.get_axis(2)
#     # velocity = math.sqrt(x_data^2 + y_data)
#     # krs_setPos_CMD(servo_ids[i], velocity)
#     ly = joy.get_axis(1)
    ry = joy.get_axis(4)
    rl = joy.get_axis(1)
    measure_up = joy.get_button(0)
    measure_down = joy.get_button(1)
    if measure_up:
        measure = 1
    elif measure_down:
        measure = -1
    else:
        measure = 0
    krs_servo.krs_setPos_CMD(krs,R_Wheel_ID, int(ry*-1*4000+7500))
    krs_servo.krs_setPos_CMD(krs,L_Wheel_ID, int(rl*4000+7500))
    krs_servo.krs_setPos_CMD(krs,measure_ID, int(measure*4000+7500))
    print(int(ry*-1*4000+7500),int(rl*4000+7500), int(measure*4000+7500))
#     krs_setPos_CMD(L_Wheel_ID, ly)

