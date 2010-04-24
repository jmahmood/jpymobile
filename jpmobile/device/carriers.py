#!/usr/bin/env python
from . import docomo
from . import au
from . import softbank
import os


def get_carriers():
    return [
        'docomo'
    ]

def factory(type):
    if type == 'docomo':
        return docomo.Docomo(os.environ)
    if type == 'au':
        return au.AU(os.environ)
    if type == 'softbank':
        return softbank.Softbank(os.environ)
