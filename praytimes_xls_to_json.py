# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 09:24:37 2015

@author: rusto
"""
import json
import datetime
"""
import xlrd

readbook = xlrd.open_workbook('pray.xls', on_demand = True, formatting_info = True)
readsheet = readbook.sheet_by_index(0)
days = []
months = []
i = 1
rownum = 0
while rownum < readsheet.nrows:
    if i ==  int(readsheet.cell_value(rownum, 0)):
        prays = []
        for colnum in range(6):
            prays.append(readsheet.cell_value(rownum, colnum + 2))
        days.append(prays)
        rownum += 1
    else:
        months.append(days)
        days = []
        i += 1
months.append(days)
print months
json.dump(months, open('test', 'w'))
"""
# current month & day
tt = datetime.datetime.now().timetuple()
month = tt[1]
day = tt[2]

# load from file
months = json.load(open('test', 'r'))
for i in range(6):
    print months[month - 1][day - 1][i]
