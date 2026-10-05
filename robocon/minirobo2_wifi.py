# -*- coding: utf-8 -*-
"""
KRS_Python_Sample_1
KONDO KAGAKU CO.,LTD.
2021/12/20
"""

import serial
import time
import math
import krs_servo
import socket
import pickle

krs = serial.Serial('/dev/ttyUSB0', baudrate=115200, parity=serial.PARITY_EVEN, timeout=0.5)
#サーボのIDを読み出します
#bl, reData = krs_servo.krs_getID_CMD(krs)
#print("ID", reData)


R_Wheel_ID = 0
L_Wheel_ID = 19
measure_ID = 1
UDP_IP = "10.22.248.71"  # 自分のIP
#UDP_IP = "192.168.2.104"
UDP_PORT = 5000     # 任意のポート番号を指定

# ソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
#     # x_data = joy.get_axis(0)
#     # y_data = joy.get_axis(1)
#     # theta_data = joy.get_axis(2)
#     # velocity = math.sqrt(x_data^2 + y_data)
#     # krs_setPos_CMD(servo_ids[i], velocity)
#     ly = joy.get_axis(1)
    byte_data, addr = sock.recvfrom(1000)
    data = pickle.loads(byte_data)
    ry = data[1]
    rl = data[4]
    if ry == 0.004:
        ry = 0
    if rl == 0.004:
        rl = 0
    measure_up = data[10]
    measure_down = data[11]
    if measure_up == 0:
        measure = 1
    elif measure_down == 0:
        measure = -1
    else:
        measure = 0
    
    krs_servo.krs_setPos_CMD(krs,L_Wheel_ID, int(rl*4000+7500))
    krs_servo.krs_setPos_CMD(krs,measure_ID, int(measure*4000+7500))
    krs_servo.krs_setPos_CMD(krs,R_Wheel_ID, int(ry*-1*4000+7500))

    print(int(ry*-1*4000+7500),int(rl*4000+7500), int(measure*4000+7500))
#     krs_setPos_CMD(L_Wheel_ID, ly)

