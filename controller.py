# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:31:05 2019

@author: claud
"""

import pyb
import utime


class Controller:
    
    
    def __init__(self, kp, setpoint):
        ''' Initializes controll loop to parameters'''

        self.kp = kp
        self.setpoint= setpoint
        self.time_list = []
        self.pos_list = []
        
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

        self.time_list.append(utime.ticks_ms())
        self.pos_list.append(position)

        return self._output
        
        
    def set_gain(self, setting_gain):
        self.kp = setting_gain
        
        
    def set_setpoint (self, setting_setpoint):
        self.setpoint = setting_setpoint
        
    def print_results (self):

        for i in range(len(self.time_list)) :
            print(str(self.time_list[i]) + ", " + str(self.pos_list[i]))

        
    
    
