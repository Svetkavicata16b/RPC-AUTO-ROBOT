function reset_position () {
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 90)
    s0 = 90
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 0)
    s1 = 0
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S2, 90)
    s2 = 90
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
}
radio.onReceivedString(function (receivedString) {
    reseave_command = parseFloat(receivedString)
    move(reseave_command)
})
input.onButtonPressed(Button.B, function () {
    again_or_no = 1
})
function degrees (servo: number, add_degrees: number) {
    rotate_servo_degrees = servo + add_degrees
    if (!(rotate_servo_degrees < 0 || rotate_servo_degrees > 180)) {
        return rotate_servo_degrees
    } else {
        return servo
    }
}
function move (command: number) {
    if (command & S1_RIGHT) {
        s0 = degrees(s0, -10)
        basic.pause(200)
    } else if (command & S1_LEFT) {
        s0 = degrees(s0, 10)
        basic.pause(200)
    }
    if (command & S2_BACK) {
        s1 = degrees(s1, -10)
        basic.pause(200)
    } else if (command & S2_FORWARD) {
        s1 = degrees(s1, 10)
        basic.pause(200)
    }
    if (command & S3_BACK) {
        s2 = degrees(s2, -10)
        basic.pause(200)
    } else if (command & S3_FORWARD) {
        s2 = degrees(s2, 10)
        basic.pause(200)
    }
    if (command & PINCH_CLOSE) {
        if (!(is_pinch_closed)) {
            wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 20)
            is_pinch_closed = 1
            basic.pause(200)
        } else {
            wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
            is_pinch_closed = 0
            basic.pause(200)
        }
    } else if (command & PINCH_OPEN) {
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 90)
        basic.pause(200)
    }
    if (command & CAR_FORWARD) {
        wuKong.setAllMotor(50, 50)
        basic.pause(200)
        wuKong.stopAllMotor()
    } else if (command & CAR_BACK) {
        wuKong.setAllMotor(-50, -50)
        basic.pause(200)
        wuKong.stopAllMotor()
    }
    if (command & CAR_RIGHT) {
        wuKong.setAllMotor(50, -50)
        basic.pause(200)
        wuKong.stopAllMotor()
    } else if (command & CAR_LEFT) {
        wuKong.setAllMotor(-50, 50)
        basic.pause(200)
        wuKong.stopAllMotor()
    }
    if (command & RESET_POSITION) {
        reset_position()
    }
    if (command == 0 && again_or_no == 1) {
        basic.pause(200)
    }
    if (again_or_no == 2) {
        command_list.push(command)
    }
    if (again_or_no == 0) {
        if (command & AGAIN) {
            again_or_no = 1
            strip.showColor(neopixel.colors(NeoPixelColors.Green))
            for (let стойност of command_list) {
                move(стойност)
            }
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
            again_or_no = 0
        }
        if (command & LISTEN) {
            command_list = []
            again_or_no = 2
            strip.showColor(neopixel.colors(NeoPixelColors.Purple))
        }
    }
    if (again_or_no == 2) {
        if (command & STOP_LISTEN) {
            again_or_no = 0
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
        }
    }
}
let rotate_servo_degrees = 0
let s2 = 0
let s1 = 0
let s0 = 0
let strip: neopixel.Strip = null
let command_list: number[] = []
let is_pinch_closed = 0
let again_or_no = 0
let reseave_command = 0
let stop = 0
let list2: number[] = []
let index = 0
reseave_command = 0
again_or_no = 0
let S1_RIGHT = 1
let S1_LEFT = 2
let S2_BACK = 4
let S2_FORWARD = 8
let S3_BACK = 16
let S3_FORWARD = 32
let PINCH_OPEN = 64
let PINCH_CLOSE = 128
let CAR_FORWARD = 256
let CAR_BACK = 512
let CAR_RIGHT = 1024
let CAR_LEFT = 2048
let AGAIN = 4096
let LISTEN = 8192
let STOP_LISTEN = 16384
let RESET_POSITION = 32768
is_pinch_closed = 0
command_list = []
reset_position()
radio.setGroup(1)
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
basic.forever(function () {
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, s0)
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, s1)
    wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S2, s2)
})
