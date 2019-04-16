# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:31:05 2019

@author: claud
"""

import pyb



class Controller:
    
    
    def __init__(self, gain, setpoint):
        ''' Initializes controll loop to parameters'''

        self.kp = kp
        self.setpoint= setpoint
        
        
    def calculate(self, position):
        ''' Computes the controll response'''
        
        # compute error and pwm output
        self._error = self.setpoint - position
        self._pwm = self.kp * self._error

        # saturation
        if (self._pwm > 100) :
            self._pwm = 100
        elif (self._pwm < -100) :
            self._pwm = -100

        return self._pwm
        
        
    def set_gain(self, setting_gain):
        self.gain = setting_gain
        
        
    def set_setpoint (self, setting_setpoint):
        self.setpoint = setting_setpoint
        
    
        
    
    
