def градуси(servo: number, добавени_градуси: number):
    global завъртяно_servo_градуси
    завъртяно_servo_градуси = servo + добавени_градуси
    if not (завъртяно_servo_градуси < 0 or завъртяно_servo_градуси > 180):
        return завъртяно_servo_градуси
    else:
        return servo

def on_received_string(receivedString):
    global command, s0, s1, s2, true_false, stop, list2
    command = parse_float(receivedString)
    if stop == 0:
        if command & S1_RIGHT:
            s0 = градуси(s0, 10)
        elif command & S1_LEFT:
            s0 = градуси(s0, -10)
        if command & S2_BACK:
            s1 = градуси(s1, 10)
        elif command & S2_FORWARD:
            s1 = градуси(s1, -10)
        if command & S3_BACK:
            s2 = градуси(s2, 10)
        elif command & S3_FORWARD:
            s2 = градуси(s2, -10)
        if command & PINCH_CLOSE:
            if not (true_false):
                wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 20)
                true_false = 1
            else:
                wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
                true_false = 0
        elif command & PINCH_OPEN:
            wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
        if command & CAR_FORWARD:
            wuKong.set_all_motor(50, 50)
            basic.pause(200)
            wuKong.stop_all_motor()
        elif command & CAR_BACK:
            wuKong.set_all_motor(-50, -50)
            basic.pause(200)
            wuKong.stop_all_motor()
        if command & CAR_RIGHT:
            wuKong.set_all_motor(50, -50)
            basic.pause(200)
            wuKong.stop_all_motor()
        elif command & CAR_LEFT:
            wuKong.set_all_motor(-50, 50)
            basic.pause(200)
            wuKong.stop_all_motor()
        if command & AGAIN:
            stop = 1
            again_f()
            list2 = []
            stop = 0
radio.on_received_string(on_received_string)

def again_f():
    global command, s0, s1, s2, true_false
    индекс = 0
    while индекс <= len(list2):
        command = list2.index(индекс)
        if command & S1_RIGHT:
            s0 = градуси(s0, 10)
        elif command & S1_LEFT:
            s0 = градуси(s0, -10)
        if command & S2_BACK:
            s1 = градуси(s1, 10)
        elif command & S2_FORWARD:
            s1 = градуси(s1, -10)
        if command & S3_BACK:
            s2 = градуси(s2, 10)
        elif command & S3_FORWARD:
            s2 = градуси(s2, -10)
        if command & PINCH_CLOSE:
            if not (true_false):
                wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 20)
                true_false = 1
            else:
                wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
                true_false = 0
        elif command & PINCH_OPEN:
            wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
        if command & CAR_FORWARD:
            wuKong.set_all_motor(50, 50)
            basic.pause(200)
            wuKong.stop_all_motor()
        elif command & CAR_BACK:
            wuKong.set_all_motor(-50, -50)
            basic.pause(200)
            wuKong.stop_all_motor()
        if command & CAR_RIGHT:
            wuKong.set_all_motor(50, -50)
            basic.pause(200)
            wuKong.stop_all_motor()
        elif command & CAR_LEFT:
            wuKong.set_all_motor(-50, 50)
            basic.pause(200)
            wuKong.stop_all_motor()
        if command == 0:
            basic.pause(200)
        индекс += 1
        индекс += 1
завъртяно_servo_градуси = 0
list2: List[number] = []
stop = 0
true_false = 0
s2 = 0
s1 = 0
s0 = 0
индекс2 = 0
list22: List[number] = []
command = 0
AGAIN = 0
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 90)
s0 = 90
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 180)
s1 = 180
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S2, 90)
s2 = 90
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
S1_RIGHT = 1
S1_LEFT = 2
S2_BACK = 4
S2_FORWARD = 8
S3_BACK = 16
S3_FORWARD = 32
PINCH_OPEN = 64
PINCH_CLOSE = 128
CAR_FORWARD = 256
CAR_BACK = 512
CAR_RIGHT = 1024
CAR_LEFT = 2048
AGAIN = 4096
true_false = 0
stop = 0
list2 = [PINCH_CLOSE, PINCH_CLOSE]
radio.set_group(1)

def on_forever():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, s0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, s1)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S2, s2)
basic.forever(on_forever)
