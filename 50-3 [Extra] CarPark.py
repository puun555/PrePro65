"""[Extra] Carpark"""
def pricecal(hour1):
    """pricecal func"""
    price = 0
    hour = hour1 - (hour1//24)*24
    dayz = hour1//24
    print('%d day %d hour' %(dayz, hour))
    if hour1 > 2:
        if hour1 >= 2 and hour1 <= 12:
            price += 15*(hour1)
        else:
            day = hour1//24
            hour1 = hour1 - (hour1//24)*24
            if hour1 > 12:
                day += 1
                hour1 = 0
            elif hour1 <= 2:
                hour1 = 0
            price += day*200 + hour1*15
            price -= (dayz//7)*300
            if dayz//28 >= 1:
                price -= 500
    else:
        price = 0
    print('%d baht' %price)
def main():
    """main func"""
    first, time_f, gob, time_b = int(input()), int(input()), int(input()), int(input())
    error = False
    if first <= gob and (first <= 365 and gob <= 365) and (first > 0 and gob > 0):
        if first == gob and (time_f <= time_b) and (time_f < 24 and time_b < 24):
            hour = time_b - time_f
        elif first < gob and (time_f < 24 and time_b < 24) and (time_f >= 0 and time_b >= 0):
            hour = (24 - time_f) + (24*(gob-first-1)) + time_b
        else:
            error = True
    else:
        error = True
    if error:
        print('error')
    else:
        pricecal(hour)
main()
