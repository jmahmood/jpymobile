#!/usr/bin/env python
import abstractmobile
import re
import os
from .. import display

class Docomo(abstractmobile.AbstractMobile, object):
    from ip_info_docomo import IP_ADDRESSES
    from display_info_docomo import DISPLAY_INFO
    USER_AGENT_REGEXP = """/^DoCoMo/"""
    MAIL_ADDRESS_REGEXP = """/^.+@docomo\.ne\.jp$/"""
    
    def __init__(self, request):
        super(Docomo, self ).__init__(request)
        self.valid = re.search(self.USER_AGENT_REGEXP, self.env['HTTP_USER_AGENT'] ) != None
    
    def areacode(self, actn=False, areacode=False):
        if actn == "OK":
            return areacode
        else:
            return False

    # They use a map class, but we don't have to
    # worry about this for now.
    def position(self, lat=False, lon=False, geo=False):
        
            

        return False
    
    def serialnumber(self):
        try:
            agent = self.env['HTTP_USER_AGENT']
            mova = re.search('/ser([0-9a-zA-Z]{11})$/',agent)
            if mova:
                return mova.group(0)
            foma = re.search('/ser([0-9a-zA-Z]{15});/',agent)
            if foma:
                return foma.group(0)
            return False
        except:
            # should really raise an "invalid serial number"
            # error, but I am not sure how to do that right
            # now.
            return False
        
    def icc(self):
        try:
            # Returns the Foma card number if it exists.
            agent = self.env['HTTP_USER_AGENT']
            icc = re.search('/icc([0-9a-zA-Z]{20})\)/',agent)
            if icc:
                return icc.group(0)
            else:
                return False
        except:
            return False

    def guid(self):
        try:
            return self.env['HTTP_X_DCMGUID']
        except:
            return False
    
    def ident_subscriber(self):
        return self.guid or self.icc
    
    
    def display(self):
        di = self.__display_info()

        if not di:
            return False

        self.display = display.Display(
            False,
            False,
            di['browser_width'],
            di['browser_height'],
            di['color_p'],
            di['colors']
        );
        return True
    
    def supports_cookie(self):
        return false
    
    def __model_name(self):
        try:
            agent = self.env['HTTP_USER_AGENT']
            docomo20 = re.search('/^DoCoMo\/2.0 (.+)\(/',agent)
            if docomo20:
                return docomo20.group(0)
            docomo10 = re.search('/^DoCoMo\/1.0\/(.+?)\//',agent)
            if docomo10:
                return docomo10.group(0)
            return False
        except:
            # should really raise an "invalid serial number"
            # error, but I am not sure how to do that right
            # now.
            return False
        
    def __display_info(self):
        try:
            return self.DISPLAY_INFO[self.__model_name()]
        except:
            return False
