#!/usr/bin/env python

class Position:
    def __init__(self):
        self.lat = None
        self.lon = None
        self.options = {}
        
    def dms2deg(self,d,m,s):
        try:
            return int(d) + float(int(m)) / 60.0 + float(s)/3600.0
        except:
            return False
    
    def tokyo2wgs84(lat, lon):
        latlon = self.tky2jgd(lat, lon)
        lat = latlon[0]
        lon = latlon[1]
    
    def to_s(self):
        print('%s%f%s%f' % 'N' if self.lat > 0 else 'S', self.lat, 'E' if self.lat > 0 else 'W', self.lon)
    