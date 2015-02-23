# -*- coding: utf-8 -*-

'''
Created on 22/feb/2015

@author: satsha
'''

import xml.etree.ElementTree as ET
from dns.rdatatype import NULL

###########################DEFAULTS############################

HTTP_SERVER_PORT = 8080
HTTP_SERVER_HOSTNAME = '0.0.0.0'
HTTP_SERIAL_PATH = '/serial'
HTTP_SERIAL_PARAMETER = 'data'
HTTPS_SERVER_KEY_PATH = '';
HTTPS_SERVER_CERTIFICATE_PATH = '';
    
SERIAL_PORT = '/dev/tty'
SERIAL_SPEED = 9600
SERIAL_WAIT_FOR_RESPONSE = False

#########################LOAD FROM XML#########################

def loadConfiguration():
    
    global HTTP_SERVER_PORT
    global HTTP_SERVER_HOSTNAME
    global HTTP_SERIAL_PATH
    global HTTP_SERIAL_PARAMETER
    global HTTPS_SERVER_KEY_PATH
    global HTTPS_SERVER_CERTIFICATE_PATH
    
    global SERIAL_PORT
    global  SERIAL_SPEED
    global  SERIAL_WAIT_FOR_RESPONSE
    
    root = NULL;
    
    try:
        tree = ET.parse('../config.xml')
        root = tree.getroot()
        
        for child in  root: 
            
            if child.tag == 'server':
                for child1 in child:
                    if child1.tag == 'url':
                        HTTP_SERIAL_PATH = child1.attrib['path']
                        HTTP_SERIAL_PARAMETER = child1.attrib['parameter']
                    elif child1.tag == 'network':
                        HTTP_SERVER_PORT = int(child1.attrib['port'])
                        HTTP_SERVER_HOSTNAME = child1.attrib['hostname']
                    elif child1.tag == 'ssl':
                        HTTPS_SERVER_CERTIFICATE_PATH = child1.attrib['certificate']
                        HTTPS_SERVER_KEY_PATH = child1.attrib['key']
            elif child.tag == 'serial':    
                SERIAL_PORT = child.attrib['port']
                SERIAL_SPEED = int(child.attrib['speed'])
                if child.attrib['wait_for_response'] == 'True':
                    SERIAL_WAIT_FOR_RESPONSE = True
                else:
                    SERIAL_WAIT_FOR_RESPONSE = False
                              
        print '##########LOADED CONFIGURATION###############\nHTTP_SERVER_PORT: '+str(HTTP_SERVER_PORT) \
        +'\nHTTP_SERVER_HOSTNAME: '+HTTP_SERVER_HOSTNAME \
        +'\nHTTP_SERIAL_PATH: '+HTTP_SERIAL_PATH \
        +'\nHTTP_SERIAL_PARAMETER: '+HTTP_SERIAL_PARAMETER \
        +'\nSERIAL_WAIT_FOR_RESPONSE: '+str(SERIAL_WAIT_FOR_RESPONSE) \
        +'\nHTTPS_SERVER_KEY_PATH: '+HTTPS_SERVER_KEY_PATH \
        +'\nHTTPS_SERVER_CERTIFICATE_PATH: '+HTTPS_SERVER_CERTIFICATE_PATH \
        +'\nSERIAL_PORT: '+SERIAL_PORT \
        +'\nSERIAL_SPEED: '+str(SERIAL_SPEED)
        
    except:    
        print '###CONFIG.XML NOT FOUND OR PARSE ERROR, USING DEFAULTS###' \
        +'\nHTTP_SERVER_PORT: '+str(HTTP_SERVER_PORT) \
        +'\nHTTP_SERVER_HOSTNAME: '+HTTP_SERVER_HOSTNAME \
        +'\nHTTP_SERIAL_PATH: '+HTTP_SERIAL_PATH \
        +'\nHTTP_SERIAL_PARAMETER: '+HTTP_SERIAL_PARAMETER \
        +'\nSERIAL_WAIT_FOR_RESPONSE: '+str(SERIAL_WAIT_FOR_RESPONSE) \
        +'\nHTTPS_SERVER_KEY_PATH: '+HTTPS_SERVER_KEY_PATH \
        +'\nHTTPS_SERVER_CERTIFICATE_PATH: '+HTTPS_SERVER_CERTIFICATE_PATH \
        +'\nSERIAL_PORT: '+SERIAL_PORT \
        +'\nSERIAL_SPEED: '+str(SERIAL_SPEED)



###############################################################