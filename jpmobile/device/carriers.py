#!/usr/bin/env python
from . import docomo
from . import au
from . import softbank


def get_carriers():
    return [
        'docomo',
        'au',
        'softbank'
    ]

def factory(type):
    if type == 'docomo':
        return docomo.Docomo()
    if type == 'au':
        return au.AU()
    if type == 'softbank':
        return softbank.Softbank()
