#!/usr/bin/env python
from ..device import carriers

def is_mobile():
    return mobile() != False
    
def mobile():
    mobilecarriers = carriers.get_carriers()
    for carrier in mobilecarriers:
        c = carriers.factory(carrier)
        if c.valid:
            return c
        else:
            return False
