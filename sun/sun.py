# -*- coding: utf-8 -*-

# source:
#    almanac for computers, 1990
#    published by nautical almanac office
#    united states naval observatory
#    washington, dc 20392

# inputs:
#    day, month, year:       date of sunrise/sunset
#    latitude, longitude:    location for sunrise/sunset
#        longitude is positive for east and negative for west
#    zenith:                 sun's zenith for sunrise/sunset
#        offical        = 90 degrees 50'
#        civil          = 96 degrees
#        nautical       = 102 degrees
#        astronomical   = 108 degrees

from datetime import date, time
#from math import floor, sin, atan, tan, degrees, radians, cos, asin, acos
from math import *
import argparse

def day_of_year(day, month, year):
    N1 = floor(275 * month / 9)
    N2 = floor((month + 9) / 12)
    N3 = (1 + floor((year - 4 * floor(year / 4) + 2) / 3))
    return N1 - (N2 * N3) + day - 30

date = date.today()
N = day_of_year(date.day, date.month, date.year)
longitude = 73.18815
latitude = 49.89362
zenith = 90.83333
localOffset = 6

#parcer = argparse.ArgumentParser(description = "description")
#parcer.add_argument('-d', '--date', action = 'store_const', dest = 'date', const = date.today(), help = 'date')
#parcer.add_argument('-lon', '--longitude', action = 'store_const', dest = 'longitude', longitude = '73.18815', help = 'longitude')
#parcer.add_argument('-lat', action = 'store', dest = 'latitude', help = 'latitude')
#parcer.add_argument('-z', action = 'store', dest = 'zenith_n', help = 'zenith')
#parcer.add_argument('-o', action = 'store', dest = 'localOffset', help = 'localoffset')

# N = day_of_year(25, 6, 1990)
# longitude = -74.3
# latitude = 40.9
# zenith = 90.50
# localOffset = -4

# convert the longitude to hour value and calculate an approximate time
lngHour = longitude / 15
# if rising time is desired
r_t = N + ((6 - lngHour) / 24)
# if setting time is desired
s_t = N + ((18 - lngHour) / 24)

# calculate the sun's mean anomaly
r_M = (0.9856 * r_t) - 3.289
s_M = (0.9856 * s_t) - 3.289

# if a > d: while a > d: a -= d
def into_range(d, a):
    if a < 0:
        while a < 0: a += d
    if a > d:
        while a > d: a -= d
    return a

# calculate the sun's true longitude
#    throughout the arguments of the trig functions (sin, tan)
#    are in degrees. it will likely be necessary to convert
#    to radians. eg sin(170.626 deg) = sin(170.626 * pi / 180 radians)
#    = 0.16287
r_L = r_M + (1.916 * sin(r_M)) + (0.020 * sin(2 * r_M)) + 282.634
r_L = into_range(360, r_L)
s_L = s_M + (1.916 * sin(s_M)) + (0.020 * sin(2 * s_M)) + 282.634
s_L = into_range(360, s_L)

# calculate the sun's right ascension
r_RA = degrees(atan(0.91764 * tan(radians(r_L))))
r_RA = into_range(360, r_RA)
s_RA = degrees(atan(0.91764 * tan(radians(s_L))))
s_RA = into_range(360, s_RA)

# right ascension value needs to be in the same quadrant as L
r_Lquadrant = (floor(r_L / 90)) * 90
r_RAquadrant = (floor(r_RA / 90)) * 90
r_RA = r_RA + (r_Lquadrant - r_RAquadrant)
s_Lquadrant = (floor(s_L / 90)) * 90
s_RAquadrant = (floor(s_RA / 90)) * 90
s_RA = s_RA + (s_Lquadrant - s_RAquadrant)

# right ascension value needs to be converted into hours
r_RA = r_RA / 15
s_RA = s_RA / 15

# calculate the sun's declination
r_sinDec = 0.39782 * sin(radians(r_L))
r_cosDec = cos(asin(r_sinDec))
s_sinDec = 0.39782 * sin(radians(s_L))
s_cosDec = cos(asin(s_sinDec))

# calculate the sun's local hour angle
r_cosH = (cos(radians(zenith)) - (r_sinDec * sin(radians(latitude)))) / (r_cosDec * cos(radians(latitude)))
s_cosH = (cos(radians(zenith)) - (s_sinDec * sin(radians(latitude)))) / (s_cosDec * cos(radians(latitude)))
# if cosH > 1
#    the sun never rises on this location (on the specified date)
if r_cosH > 1:
    print "the sun never rises on this location (on the specified date)"
# if cosH < -1
#    the sun never sets on this location (on the specified date)
if s_cosH < -1:
    print "the sun never sets on this location (on the specified date)"

# finish calculating H and convert into hours
# if rising time is desired
r_H = 360 - degrees(acos(r_cosH))
r_H = r_H / 15
# if setting time is desired
s_H = degrees(acos(s_cosH))
s_H = s_H / 15

# calculate local mean time of rising/setting
r_T = r_H + r_RA - (0.06571 * r_t) - 6.622
s_T = s_H + s_RA - (0.06571 * s_t) - 6.622

# adjust back to utc
r_UT = r_T - lngHour
r_UT = into_range(24, r_UT)
s_UT = s_T - lngHour
s_UT = into_range(24, s_UT)

# convert ut value to local time zone of latitude/longitude
r_localT = into_range(24, r_UT + localOffset)
s_localT = into_range(24, s_UT + localOffset)

#print r_localT, s_localT
#parser.parce_args()
print "sunrise:"
print('%2d:%2d:%2d' % (r_localT // 1, r_localT % 1 * 60, (r_localT % 1 * 60) % 1 * 60))
print "sunset:"
print('%2d:%2d:%2d' % (s_localT // 1, s_localT % 1 * 60, (s_localT % 1 * 60) % 1 * 60))
