'''
    Time Conversion problem

    https://www.hackerrank.com/challenges/time-conversion
'''
import sys


def Solution():
    time = raw_input().strip()

    hh, mm, ssA = time.split(':')
    ss = ssA[:2]
    isAm = ssA[2:] == "AM"
    if isAm:
        if int(hh) >= 12:
            hh = "00"
        print hh + ":" + mm + ":" + ss
    else:
        hh = str(int(hh) + 12)
        if int(hh) >= 24:
            hh = "12"
        print hh + ":" + mm + ":" + ss
Solution()
