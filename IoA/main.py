# -*- coding: utf-8 -*-

'''
Created on 22/feb/2015

@author: satsha
'''

import IoA.Configuration as conf
import IoA.server.HttpServer as server
from IoA.seriaL.SerialInterface import SerialInterface as serial

def main():
    conf.loadConfiguration()
    serialInterface = serial()
    
    if serialInterface.start():
        
        server.start(serialInterface)
    

if __name__ == '__main__':
    main()