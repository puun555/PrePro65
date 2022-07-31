"""Late Meeting CR:P'ทิว"""

def main():
    """time"""
    hour = int(input())
    minute = int(input())
    second = int(input())
    pm_am = input()
    minute_out = int(input())
    second_out = int(input())
    second = second+second_out
    if pm_am == "pm":
        if hour == 12:
            hour24 = 12
        else: hour24 = hour+12
    elif pm_am == "am":
        if hour == 12:
            hour24 = 0
        else: hour24 = hour
    minute = minute+(second//60)
    second = second-60*(second//60)
    minute = minute+minute_out
    hour24 = hour24+(minute//60)
    minute = minute-60*(minute//60)
    if 12 > hour24%24 >= 0:
        pm_am = pm_am.replace("pm", "am")
        hour2 = hour24%24
        if hour2 == 0:
            hour2 = 12
    elif 24 >= hour24%24 >= 12:
        pm_am = pm_am.replace("am", "pm")
        hour2 = hour24%24-12
        if hour2 == 0:
            hour2 = 12
    print("%02d:%02d:%02d %s"%(hour2, minute, second, pm_am))
main()
