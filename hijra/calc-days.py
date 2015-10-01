#!/usr/bin/env python

# the first day of Hijrah [1 Muharram] 622, the year
# of the Gregorian calendar [16 June]
#print "Gregorian calendar:"

# 16 June - 31 December 622
day = 168

year = 623

while year < 2014:
    if year % 4 == 0:
        day += 366
#        print year, "leap year"
    else:
        day += 365
#        print year, "standart year"

    print (day)
    year += 1

# 1 January - 4 July 2014
day += 185
print (day)

#day = 508406

orig_day = day

print "Hijrah calendar:"

print "turkish cycle:"
year = 0
while day > 355:
    if (year % 8 == 2) or (year % 8 == 5) or (year % 8 == 7):
        day -= 355
#        print year, "leap year"
    else:
        day -= 354
#        print year, "standart year"

    year += 1

day -= 236
print (day)

day = orig_day

print "arab cycle:"
year = 0
while day > 355:
    if (year % 30 == 2) or (year % 30 == 5) or (year % 30 == 7) or (year % 30 == 10) or (year % 30 == 13) or (year % 30 == 16) or (year % 30 == 18) or (year % 30 == 21) or (year % 30 == 24) or (year % 30 == 26) or (year % 30 == 29):
        day -= 355
#        print year, "leap year"
    else:
        day -= 354
#        print year, "standart year"

    year += 1

day -= 236
print (day)
