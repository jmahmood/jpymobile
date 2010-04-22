#!/usr/bin/env python
from ..device import carriers
import os

def is_mobile():
    return mobile(str) != False
    
def mobile():
    mobilecarriers = carriers.get_carriers()
    for carrier in mobilecarriers:
        c = carriers.factory(carrier)
        user_agent = user_agent()
        if c.check(user_agent):
            return c
        else:
            return False

def user_agent():
    return os.environ['HTTP_USER_AGENT']

