"""Cr. P'Few"""
def main(_, going, time):
    """function main"""
    hour = int(time[:2])
    minute = int(time[3:5])
    am_pm = time[-2:]
    if going[-4:-1] == "SYD":
        hour += 12
    elif going[-4:-1] == "SGN":
        hour += 1
        minute += 50
    elif going[-4:-1] == "ATL":
        hour += 9
        minute += 55
    elif going[-4:-1] == "YVR":
        hour += 2
        minute += 20
    elif going[-4:-1] == "KTM":
        hour += 11
        minute += 45
    hour += am_pm == "PM" and int(time[:2]) != 12 and 12 or am_pm == "AM" \
and int(time[:2]) == 12 and -12
    hour += minute//60
    minute = minute%60
    hour = hour%24
    am_pm = 0 <= hour < 12 and "AM" or "PM"
    hour = hour%12
    print("BKK - %s"%going[-4:-1])
    print("%02d:%02d %s"%(hour == 0 and 12 or hour, minute, am_pm))
main(input(), input(), input())
