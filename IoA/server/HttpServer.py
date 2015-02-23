# -*- coding: utf-8 -*-
'''
Created on 22/feb/2015

@author: satsha
'''


import web
from dns.rdatatype import NULL
from web.wsgiserver import CherryPyWSGIServer
import IoA.Configuration as conf

###############################################################

urls = NULL
serial = NULL;

###############################################################

class HttpServer(web.application):
    def run(self, *middleware):
        
        self.SSL = False
        
        if conf.HTTPS_SERVER_KEY_PATH != '' and conf.HTTPS_SERVER_CERTIFICATE_PATH != '':
            CherryPyWSGIServer.ssl_certificate = conf.HTTPS_SERVER_CERTIFICATE_PATH
            CherryPyWSGIServer.ssl_private_key = conf.HTTPS_SERVER_KEY_PATH
            self.SSL = True

        if self.SSL:            
            print '################HTTP SERVER##################\nserver started @ https://'+conf.HTTP_SERVER_HOSTNAME+':'+str(conf.HTTP_SERVER_PORT)+urls[0]
        else:
            print '################HTTP SERVER##################\nserver started @ http://'+conf.HTTP_SERVER_HOSTNAME+':'+str(conf.HTTP_SERVER_PORT)+urls[0]

        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, (conf.HTTP_SERVER_HOSTNAME, conf.HTTP_SERVER_PORT))
        
###############################################################

class Paths:
                
    def GET(self):
        
        if(serial != NULL):
            self.parameters = web.input()
            
            self.response = ('{"response":"invalid parameter"}')
            
            try:
                serial.send(self.parameters[conf.HTTP_SERIAL_PARAMETER]+'\n')
                
                if conf.SERIAL_WAIT_FOR_RESPONSE:
                    self.response = ('{"response":"'+serial.readline()+'"}')
                else:
                    self.response = ('{"response": "data sent to '+conf.SERIAL_PORT+'"}')
                
            except:
                pass
            
            return self.response

###############################################################

def start(s):
    
    global serial
    global urls
    
    urls = (conf.HTTP_SERIAL_PATH,'Paths')
    
    serial = s
    app = HttpServer(urls, globals())
    app.run()
    
    