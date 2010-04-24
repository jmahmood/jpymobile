#!/usr/bin/env python

class AbstractMobile:
    def __init__(self, request):
        self.env = request
        self.valid = False

    def position(self):
        return False
    
    def ident(self):
        return self.ident_subscriber() or self.ident_device()
        
    def ident_subscriber(self):
        return
    
    def ident_device(self):
        return
    
    def valid_ip(self, remote_address):
        addresses = self.IP_ADDRESSES
        return remote_address in addresses
    
    # This will return a display class instance.
    # We do not support that yet.
    def display(self):
        return False
    
    def supports_cookie(self):
        return False
    
    def params(request):
        return getattr(self, request)
    