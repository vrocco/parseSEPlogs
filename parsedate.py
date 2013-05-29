
#This script is to parse the date/time stamp from Symantec Endpoint Protection logs. It takes a single input of six hexadecimal octets.
#The hex value is stored in the very first comma delimited field of each line in the log files.
#Usage: pasredate.py <hex datestamp>
#
#
#Created by: Vito Rocco

import sys, getopt

def year (hex):
    yr = int(hex[0:2], 16)
    yr += 1970
    return str(yr)

def month (hex):
    m = int(hex[2:4], 16)
    if m == 0:
        m = "January"
        return m
    elif m == 1:
        m = "February"
        return m
    elif m == 2:
        m = "March"
        return m
    elif m == 3:
        m = "April"
        return m
    elif m == 4:
        m = "May"
        return m
    elif m == 5:
        m = "June"
        return m
    elif m == 6:
        m = "July"
        return m
    elif m == 7:
        m = "August"
        return m
    elif m == 8:
        m = "September"
        return m
    elif m == 9:
        m = "October"
        return m
    elif m == 10:
        m = "November"
        return m
    else:
        m = "December"
        return m
		
def day (hex):
    d = int(hex[4:6], 16)
    return str(d)

def hour (hex):
    hr = int(hex[6:8], 16)
    if hr < 10:
        return "0" + str(hr)
    else:
        return str(hr)

def minute (hex):
    min = int(hex[8:10], 16)
    if min < 10:
        return "0" + str(min)
    else:
        return str(min)

def second (hex):
    sec = int(hex[10:12], 16)
    if sec < 10:
        return "0" + str(sec)
    else:
        return str(sec)
		
def formatdate ():
	date = month(hex) + " " + day(hex) + ", " + year(hex) + " " + hour(hex) + ":" + minute(hex) + ":" + second(hex)
	return date


if len(sys.argv) < 2:
	sys.stdout.write ("Usage: parsedate.py <hex datestamp>")
else:
	hex = sys.argv[1]
	sys.stdout.write (formatdate())
