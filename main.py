import controller
import encoder
import motor
import pyb
import utime

def main():
    control = controller.Controller(1, 5000)
    motor1 = motor.MotorDriver()
    encoder1 = encoder.Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, pyb.Timer(4))
    control_duration = 300

    while True:
        key = input("press a")

        print("you typed: " + key)
        key_float = 0.
        try:
            key_float = float(key)
        except:
            print("not a float")
        
        if key == "a":
            start_time = utime.ticks_ms()
            encoder1.zero()
            control.clear_list()
            while (start_time + control_duration) > utime.ticks_ms():
                pwm = control.calculate(encoder1.get_position())
                motor1.set_duty_cycle(pwm)
            
            control.print_results()
        elif (key_float):
            print("setting gain to: " + str(key_float))
            control.set_gain(key_float)
            
        key = None
        
        
        
if __name__ == '__main__':
    main()
    
