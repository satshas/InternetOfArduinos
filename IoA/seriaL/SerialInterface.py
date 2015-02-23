# -*- coding: utf-8 -*-
'''
Created on 22/feb/2015

@author: satsha
'''

import serial
import IoA.Configuration as conf

class SerialInterface(object):
    def start(self):
        
        print '#############SERIAL INTERFACE################'

        try:
            self.serialInterface = serial.Serial(conf.SERIAL_PORT, conf.SERIAL_SPEED)
            self.init = True;
            print 'serial initialized @ '+conf.SERIAL_PORT+' speed of '+str(conf.SERIAL_SPEED)
            return True
        
        except:
            print 'serial initizialization error @ '+conf.SERIAL_PORT+' speed of '+str(conf.SERIAL_SPEED)
            return False
    
    def send(self,data):
        
        if self.init:
            self.serialInterface.write(str(data))
            
    def readline(self):
        
        try:
            
            if self.init:
                return self.serialInterface.readline().replace('\n','').replace('\r','')
            
        except:
            pass
        
