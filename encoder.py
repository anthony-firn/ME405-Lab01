## @file encoder.py
#  Brief doc for encoder.py
#
#  Detailed doc for encoder.py 
#
#  @author Your Name
#
#  @copyright License Info
#
#  @date January 1, 1970
#
import pyb

class Encoder:
    '''
    An encoder driver object
    
    @author Your Name
    @copyright License Info
    @date January 1, 1970
    '''
    

    def __init__(self, pin1, pin2, timer):
        '''
        Constructor for encoder driver
        
        Detailed info on encoder driver constructor
        '''
        self.pinA = pyb.Pin (pin1, pyb.Pin.IN)

        self.pinB = pyb.Pin (pin2, pyb.Pin.IN)
    
        self.tim = timer
		
        self.tim.init(prescaler= 0, period= 0xFFFF)
    
        ch2 = self.tim.channel (2, pyb.Timer.ENC_A, pin = self.pinA)
        ch1 = self.tim.channel (1, pyb.Timer.ENC_B, pin = self.pinB)    
        
        self.current_ticks = 0
        self.past_ticks = 0
        self.total = 0
        self.tim.counter(0)


    def get_position(self):
        '''
        Gets the encoder's position
        
        Detailed info on encoder get_position method
        '''
        self.past_ticks = self.current_ticks
        self.current_ticks = self.tim.counter()
        self.delta_ticks = self.current_ticks - self.past_ticks
        if self.delta_ticks > 32768:
            self.delta_ticks -= 65536
            
        elif self.delta_ticks < -32768:
            self.delta_ticks += 65536
            
        self.total += self.delta_ticks
        return self.total
        

    def zero(self):
        '''
        Zeros out the encoder
        
        Detailed info on encoder zero function
        '''
        self.current_ticks = 0
        self.past_ticks = 0
        self.total = 0
        self.tim.counter(0)
