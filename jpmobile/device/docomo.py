#!/usr/bin/env python
import abstractmobile

class Docomo(abstractmobile.AbstractMobile):
    #IP_ADDRESSES = pickle.loads('z_ip_addresses_docomo.txt')
    #DISPLAY_INFO = pickle.loads('')
    USER_AGENT_REGEXP = """/^DoCoMo/"""
    MAIL_ADDRESS_REGEXP = """/^.+@docomo\.ne\.jp$/"""
    
    # オープンiエリアがあればエリアコードを +String+ で返す。無ければ +nil+ を返す。
    def areacode(self, params):
        if params["ACTN"] == "OK":
            return params["AREACODE"]
        else:
            return False

    def position(self, lat=False, lon=False, geo=False):
        return False
        