import sg90

import serial
import time
import pygame
import math

pygame.init()
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()

while True:
    pygame.event.pump()

    ry = joy.get_axis(4)
    rl = joy.get_axis(1)
    measure_up = joy.get_button(0)
    measure_down = joy.get_button(1)

#     krs_setPos_CMD(L_Wheel_ID, ly)

