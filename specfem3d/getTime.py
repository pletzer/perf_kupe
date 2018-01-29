from datetime import datetime
import sys
import re

mon2Num = {
  'Jan': 1,
  'Feb': 2,
  'Mar': 3,
  'Apr': 4,
  'May': 5,
  'Jun': 6,
  'Jul': 7, 
  'Aug': 8,
  'Sep': 9,
  'Oct': 10,
  'Nov': 11,
  'Dec': 12,
}

d0 = sys.argv[1]
d1 = sys.argv[2]

def getDateTime(d):
    # Sun Jan 28 22:34:19 UTC 2018
    m = re.match(r'(\w+)\s+(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<hour>\d+)\:(?P<minute>\d+)\:(?P<second>\d+)\s+UTC\s+(?P<year>\d+)', d)
    if m:
        year = int(m.group('year'))
        month = mon2Num[m.group('month')]
        day = int(m.group('day'))
        hour = int(m.group('hour'))
        minute = int(m.group('minute'))
        second = int(m.group('second'))
        return datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    else:
      print 'ERROR: could not parse ', d

d0 = sys.argv[1]
d1 = sys.argv[2]

print (getDateTime(d1) - getDateTime(d0)).seconds, ' (s)'
    
