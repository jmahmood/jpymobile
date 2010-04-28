#!/usr/bin/env python
import DatumConv

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
        latlon = DatumConv.tky2jgd(lat, lon)
        lat = latlon[0]
        lon = latlon[1]
    
    def __str__(self):
        try:
            print('%s%f%s%f' %
                  ('N' if self.lat > 0 else 'S',
                  float(self.lat),
                  'E' if self.lat > 0 else 'W',
                  float(self.lon)))
        except:
            print("Attempted to print an invalid position class.")

    def ll(self):
        try:
            print("#%f,#%f" %(float(self.lat), float(self.lon)))
        except:
            print("Attempted to print an invalid position class.")
    
    def __eq__(self, other):
        try:
            return self.lat == other.lat and self.lon == other.lon
        except:
            return False

    def __ne__(self, other):
        try:
            return not self.__eq__(other)
        except:
            return False
        