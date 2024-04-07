def градуси(servo: number, добавени_градуси: number):
    global завъртяно_servo_градуси
    завъртяно_servo_градуси = servo + добавени_градуси
    if not (завъртяно_servo_градуси < 0 or завъртяно_servo_градуси > 180):
        return завъртяно_servo_градуси
    else:
        return servo

def on_received_string(receivedString):
    global reseave_command
    reseave_command = parse_float(receivedString)
    move(reseave_command)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global again_or_no
    again_or_no = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def move(command: number):
    global s0, s1, s2, true_false, again_or_no, command_list
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
    if again_or_no == 2:
        command_list.append(command)
    if again_or_no == 0:
        if command & AGAIN:
            again_or_no = 1
            strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
            for стойност in command_list:
                move(стойност)
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            again_or_no = 0
        if command & LISTEN:
            command_list = []
            again_or_no = 2
            strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    if again_or_no == 2:
        if command & STOP_LISTEN:
            again_or_no = 0
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
завъртяно_servo_градуси = 0
strip: neopixel.Strip = None
command_list: List[number] = []
true_false = 0
again_or_no = 0
s2 = 0
s1 = 0
s0 = 0
reseave_command = 0
индекс = 0
list2: List[number] = []
reseave_command = 0
stop = 0
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 90)
s0 = 90
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 180)
s1 = 180
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S2, 80)
s2 = 90
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
again_or_no = 0
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
LISTEN = 8192
STOP_LISTEN = 16384
true_false = 0
command_list = []
radio.set_group(1)
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))

def on_forever():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, s0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, s1)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S2, s2)
basic.forever(on_forever)
