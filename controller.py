# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:31:05 2019

@author: claud
"""

import pyb



class Controller:
    
    
    def __init__(self, kp, setpoint):
        ''' Initializes controll loop to parameters'''

        self.kp = kp
        self.setpoint= setpoint
        
        
    def calculate(self, position):
        ''' Computes the controll response'''
        
        # compute error and output
        self._error = self.setpoint - position
        self._output = self.kp * self._error

        # saturation
        if (self._output > 100) :
            self._output = 100
        elif (self._output < -100) :
            self._output = -100

        return self._output
        
        
    def set_gain(self, setting_gain):
        self.gain = setting_gain
        
        
    def set_setpoint (self, setting_setpoint):
        self.setpoint = setting_setpoint
        
    
        
    
    
