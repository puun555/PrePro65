"""Car Park CR:P'Big(นายวิชัย คำมงคุณ)"""

def cal_hour(hour_in, hour_out, ans_number):
    """555+"""
    count = ans_number
    if hour_in < 24 and hour_out < 24:
        if hour_in != hour_out:
            hour_in = (hour_in+1) % 24
            count += 1
            return cal_hour(hour_in, hour_out, count)
        else:
            if count == 0:
                return 0
            return count

def time_price(time):
    """444+"""
    if time <= 2:
        return 0
    elif time <= 12:
        return time*15
    else:
        return 0

def day_price(day, get_time_price, check_add):
    """999+"""
    total = ((day+check_add) * 200) + get_time_price
    total = total - ((day // 7) * 300)
    total = total - ((day // 28 >= 1) * 500)
    return total

def main():
    """run555+"""
    day_in = int(input())
    time_in = int(input())
    day_out = int(input())
    time_out = int(input())

    total_day = 0
    total_hour = 0
    if (day_out == day_in) and (time_in <= time_out) and (day_in >= 1 and day_out >= 1)\
            and (time_in < 24 and time_out < 24)\
            and (day_in > 0 and day_out > 0) and (day_in <= 365 and day_out <= 365):
        check = cal_hour(time_in, time_out, 0)
        total_hour = check
        print("%d day %d hour" % (total_day, total_hour))
        return print("%d baht" % ((total_day * 200) + time_price(total_hour)))

    elif (day_in < day_out) and (day_in >= 1 and day_out >= 1)\
            and (time_in < 24 and time_out < 24) and (day_in > 0 and day_out > 0)\
            and (day_in <= 365 and day_out <= 365):
        day_in = ((day_in) * 24) + time_in
        day_out = (day_out * 24) + time_out
        total_day = (day_out - day_in) // 24
        total_hour = (day_out - day_in) - (total_day * 24)
        if total_hour > 12:
            total_time = time_price(total_hour)
            total = day_price(total_day, total_time, 1)
            print("%d day %d hour" % (total_day, total_hour))
            return print("%d baht" % total)
        total_time = time_price(total_hour)
        total = day_price(total_day, total_time, 0)

        print("%d day %d hour" % (total_day, total_hour))
        print("%d baht" % total)
    else:
        print("error")

main()
