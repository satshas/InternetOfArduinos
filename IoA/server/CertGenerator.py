# -*- coding: utf-8 -*-
'''
Created on 22/feb/2015

@author: satsha
'''

from OpenSSL import crypto, SSL
from os.path import exists, join
from pprint import pprint
from socket import gethostname
from time import gmtime, mktime


CERT_FILE = "myapp.crt"
KEY_FILE = "myapp.key"


def create_self_signed_cert(cert_dir):
    """
    If datacard.crt and datacard.key don't exist in cert_dir, create a new
    self-signed cert and keypair and write them into that directory.
    """

    if not exists(join(cert_dir, CERT_FILE)) \
            or not exists(join(cert_dir, KEY_FILE)):
            
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "Country"
        cert.get_subject().ST = "Region"
        cert.get_subject().L = "City"
        cert.get_subject().O = "Company"
        cert.get_subject().OU = "Organization"
        cert.get_subject().CN = gethostname()
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha1')

        open(join(cert_dir, CERT_FILE), "wt").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        open(join(cert_dir, KEY_FILE), "wt").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
        
if __name__ == '__main__':
   create_self_signed_cert('../../')