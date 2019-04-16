import controller
import encoder
import motor
import pyb

def main():
    control = controller.Controller(1, 1000)
    motor1 = motor.MotorDriver()
    encoder1 = encoder.Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, pyb.Timer(4))
    
    while True:
        pwm = control.calculate(encoder1.get_position())
        motor1.set_duty_cycle(pwm)
        
        
        
if __name__ == '__main__':
    main()
    
