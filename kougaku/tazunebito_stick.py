import wiringpi as wp
import socket
import json
import math
LED1 =19
localaddr = ("10.22.253.100",50000)

target_lati = 35.10321329575153
target_longi =  137.14717642312107

sock = socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
sock.bind(localaddr)

wp.wiringPiSetupGpio()
wp.pinMode(LED1,1)
wp.digitalWrite(LED1,1)
while True:
    raw_data,cli_addr = sock.recvfrom(1024)
    data = json.loads(raw_data.decode('utf-8'))
    if data["device"]["uuid"]:
        stick_lati = data["sensordata"]["gps"]["latitude"]
        stick_longi =  data["sensordata"]["gps"]["longitude"]
        stick_dir = data["sensordata"]["compass"]["compass"]
    else:
        target_lati = data["sensordata"]["gps"]["latitude"]
        target_longi =  data["sensordata"]["gps"]["longitude"]
        target_dir = math.degrees(math.atan2(target_lati - stick_lati,target_longi - stick_longi))
        
        if target_dir  > 90:
            target_dir = 450 - target_dir
        else :
            target_dir = - (target_dir - 90)
            
    target_dir = math.degrees(math.atan2(target_lati - stick_lati,target_longi - stick_longi))

    if target_dir  > 90:
        target_dir = 450 - target_dir
    else :
        target_dir = - (target_dir - 90)

    dir_err = target_dir - stick_dir
    print(target_dir,dir_err)
