import controller
import encoder
import motor
import pyb
import utime

def main():
    control = controller.Controller(1, 1000)
    motor1 = motor.MotorDriver()
    encoder1 = encoder.Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, pyb.Timer(4))
    control_duration = 100

    while True:
        key = input("press a")
        print(key)
        if key == "a":
            print("get here")
            start_time = utime.ticks_ms()
            print("start" + str(start_time))
            while (start_time + control_duration) > utime.ticks_ms():
                print( "current time" + str(utime.ticks_ms))
                pwm = control.calculate(encoder1.get_position())
                motor1.set_duty_cycle(pwm)
                key = None
        
        
        
if __name__ == '__main__':
    main()
    
