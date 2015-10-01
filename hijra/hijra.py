# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:56:31 2015

@author: rusto
"""

import math
import calendar
import datetime

weekDays = ["al-Ithnayn", "ath-Thulāthāʼ", "al-Arbi‘ā’", "al-Khamīs", "al-Jumu‘ah", "as-Sabt", "al-Aḥad"]
months = ["Muḥarram", "Ṣafar", "Rabī‘ al-Awwal", "Rabī‘ ath-Thānī", "Jumādá al-Ūlá", "Jumādá ath-Thāniyah", "Rajab", "Sha‘bān", "Ramaḍān", "Shawwāl", "Dhū al-Qa‘dah", "Dhū al-Ḥijjah"]

dateTime = datetime.datetime.now()
timeTuple = dateTime.timetuple()
year    = timeTuple[0]
month   = timeTuple[1]
day     = timeTuple[2]
hours   = timeTuple[3]
minutes = timeTuple[4]
seconds = timeTuple[5]

epoch = 2451545.0 # 1 january 2000 18:00
#epoch = 2400000.5
fractionalMonth = 29.53058796

def julian_day(year, month, day):
	if month <= 2:
		year -= 1
		month += 12
	A = math.floor(year / 100)
	B = 2 - A + math.floor(A / 4)
	return math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5

def sin(d): return math.sin(math.radians(d))
def cos(d): return math.cos(math.radians(d))
def tan(d): return math.tan(math.radians(d))

def arcsin(x): return math.degrees(math.asin(x))
def arccos(x): return math.degrees(math.acos(x))
def arctan(x): return math.degrees(math.atan(x))

def arccot(x): return math.degrees(math.atan(1.0/x))
def arctan2(y, x): return math.degrees(math.atan2(y, x))

def fixangle(angle): return fix(angle, 360.0)
def fixhour(hour): return fix(hour, 24.0)

def fix(a, mode):
	if math.isnan(a):
		return a
	a = a - mode * (math.floor(a / mode))
	return a + mode if a < 0 else a





def moon(jd):
    T = (jd - epoch) / 36525.0
    mE = 297.8502042 + T * 445267.1115168 - math.pow(T, 2) * 0.0016300 + math.pow(T, 3) / 545868.0 - math.pow(T, 4) / 113065000
    mA = 134.9634114 + T * 477198.8676313 + math.pow(T, 2) * 0.0089970 + math.pow(T, 3) / 69699.0 - math.pow(T, 4) / 863310000.0
    SmA = 357.5291092 + T * 35999.0502909 - math.pow(T, 2) * 0.0001536 + math.pow(T, 3) / 24490000
    D = fixangle(mE)
    S = fixangle(SmA)
    M = fixangle(mA)
    phaseAngle = 180 - D - 6.289 * sin(M) + 2.1 * sin(S) - 1.274 * sin(fixangle(2 * D) - M) - 0.658 * sin(2 * D)
    phaseAngle += -0.214 * sin(2 * M) 
    phaseAngle += -0.110 * sin(D)
    iF = (1 + cos(phaseAngle)) / 2 * (phaseAngle / math.fabs(phaseAngle))
    return iF

def pcision(F):
    # calculate moon day
    ### add sunset - sunrise
    ### if now > sunset: day += 1
    print F
    status = True
    Dn = 0
    jDn = F
    if moon(jDn - 1) <= 0: 
        jDn -= 1
        Dn += 1
    while status:
        Fn = moon(jDn)
        Fn2 = moon(jDn - 1)
        if ((Fn / math.fabs(Fn)) * (Fn2 / math.fabs(Fn2))) == 1:
            Dn += 1
            jDn -= 1
        else:
            if math.fabs(Fn * Fn2) < 0.2: status = False
            else:
                Dn += 1
                jDn -= 1
    print Dn
    return Dn




deltadays = julian_day(year, month, day) - julian_day(year, 1, 1)
fractionalYear = (year + deltadays / (365 + calendar.isleap(year)) - 621.578082192) / 0.97022298
fractionalYear += math.floor(math.fabs(fractionalYear) / 3000) * 30 / 10631
fractionalDay = fractionalYear - math.floor(fractionalYear)

hijraYear = fractionalYear - fractionalDay

if ((fractionalDay * 10631 / 30) - math.floor(fractionalDay * 10631 / 30) < 0.5):
    fractionalDay = math.floor(fractionalDay * 10631 / 30) + 1
else: fractionalDay = math.floor(fractionalDay * 10631 / 30) + 2

h_day_n = fractionalDay
g_year = hijraYear * 0.970224044 + 621.574981435
g_year_df = g_year - math.floor(g_year)
g_year -= g_year_df
g_day = math.floor((365 + calendar.isleap(g_year)) * g_year_df) + 1
g_year += g_day / (365 + calendar.isleap(g_year))
h_year = (g_year - 621.574981435) / 0.970224044
h_day_f = h_year - math.floor(h_year)
h_day = h_day_f * 10631 / 30 + 1;
h_month = 1
h_day_f = 1
while h_day_f < h_day_n:
    h_day += 1
    h_day_f += 1
    if h_day >= fractionalMonth:
        h_day = h_day - fractionalMonth
        h_month += 1
HDAY = math.floor(h_day) + 1
HMONTH = h_month

hijraDay = HDAY
hijraMonth = HMONTH
if hijraMonth == 13:
    hijraMonth = 1
    hijraYear += 1
partDay = (hours + minutes / 60 + seconds / 3600) / 24
precise = pcision(julian_day(year, month, day) + partDay)
if hijraDay != precise:
    if (hijraDay == 1) and (precise > 28):
        hijraMonth -= 1
        if hijraMonth == 0: 
            hijraMonth = 12
            hijraYear -= 1
    elif (hijraDay > 28) and (precise < 3):
        hijraMonth += 1
        if hijraMonth == 13:
            hijraMonth = 1
            hijraYear += 1
hijraDay = precise
if hijraYear < 1: hijraYear -= 1

print weekDays[timeTuple[6]]
print str(hijraDay) + " " + months[hijraMonth - 1] + " " + str(hijraYear)