#!/usr/bin/env python

"""From http://en.wikipedia.org/wiki/Wikipedia_talk:WikiProject_Geographical_coordinates/Archive_6:

We have 2 reference frames in Japan. One is international one,
Japanese Geodetic Datum2000, almost equal to ITRF and WGS84.
Another one is Tokyo Datum (Tokyo 97), old one. The both differences
of latitude and longitude are about 8-15 seconds.

http://vldb.gsi.go.jp/sokuchi/coordinates/localtrans.html


Some web services in Japan use Tokyo Datum (including Goog maps)"""

import math

GRS80 = [6378137, 298.257222101]
Bessel = [6377397.155, 299.152813]
Tokyo97toITRF94 = [-146.414, 507.337, 680.507]
ITRF94toTokyo97 = [ 146.414,-507.337,-680.507]
Deg2Rad = math.pi / 180

# Transforms Latitude (degrees), Longitude (degrees) and Altitude/Height (meters) coordinates into "3d orthogonal" co-ordinates.
# I have no idea what datum is.  
def blh2xyz(b_deg,l_deg,he,datum):
    a = float(datum[0])
    f = 1.0/datum[1]
    b = b_deg * Deg2Rad
    l = l_deg * Deg2Rad
    
    e2 = f * (2 - f)
    n = a / math.sqrt( 1 - e2 * math.sin(b) ** 2 );
    x = (n + he)* math.cos(b) * math.cos(l)
    y = (n+he)*math.cos(b)*math.sin(l)
    z = (n*(1-e2)+he)*math.sin(b)
    return x,y,z


# The inverse of blh2xyz.
# Converts 3d Orthogonal co-ordinates into Latitude / Longitude / Altitude
def xyz2blh(x,y,z,datum):
    a = float(datum[0])
    f = 1.0/datum[1]
    e2 = f * (2 - f)
    l = math.atan2(y,x)
    p = math.sqrt(x**2+y**2)
    r = math.sqrt(p**2+z**2)
    u = math.atan2(z*((1-f)+e2*a/r),p)
    b = math.atan2(z*(1-f)+e2*a*math.sin(u)**3,(1-f)*(p-e2*a*math.cos(u)**3))

    he = p*math.cos(b) + z*math.sin(b) - a*math.sqrt(1-e2*math.sin(b)**2)
    b_deg = b / Deg2Rad
    l_deg = l / Deg2Rad
    return b_deg,l_deg,he

# Shift a 3d Orthogonal tuple by the value of another.
def xyz2xyz(x,y,z,d):
    return x+d[0],y+d[1],z+d[2]

# Switch from Tokyo97 to WGS 84 
def tky2jgd(b,l,he=0):
    x,y,z = blh2xyz(b,l,he,Bessel)
    x,y,z = xyz2xyz(x,y,z,Tokyo97toITRF94)
    b,l,he = xyz2blh(x,y,z,GRS80)
    return b,l,he

# Switch from WGS 84 to Tokyo97.
def jgd2tky(b,l,he=0):
    x,y,z = blh2xyz(b,l,he,GRS80)
    x,y,z = xyz2xyz(x,y,z,ITRF94toTokyo97)
    b,l,he = xyz2blh(x,y,z,Bessel)
    return b,l,he
