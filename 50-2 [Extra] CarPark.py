"""Carpark CR:P'นางสาวกรกมล วิชชุธีระกุล"""

def anshour(num):
    """hour"""
    sol = 0
    if 2 < num <= 12:
        sol = num*15
    elif 12 < num <= 23:
        sol = 200
    return int(sol)

def main():
    """Car park ma leaw"""
    day = int(input())
    time = int(input())
    day2 = int(input())
    time2 = int(input())
    sol = int(((day2*24)+time2) - ((day*24)+time))
    if 0 <= sol <= 8760 and 0 <= time <= 23 and 0 <= time2 <= 23 and\
    1 <= day <= 365 and 1 <= day2 <= 365:
        ans_day = int(sol//24)
        hour = int(sol%24)
        print("%d day %d hour" %(ans_day, hour))
        if ans_day == 0 and 0 <= hour <= 2:
            print("0 baht")
        elif ans_day == 0 and 2 < hour <= 12:
            sol = hour*15
            print("%d baht" %sol)
        elif 0 <= ans_day <= 6:
            sol = (ans_day*200)+anshour(hour)
            print("%d baht" %sol)
        elif 0 <= ans_day <= 6:
            sol = (ans_day*200)+anshour(hour)
            print("%d baht" %sol)
        elif 7 <= ans_day <= 365 and 0 < ans_day//7 <= 3:
            sol = (ans_day*200)-((ans_day//7)*300)+anshour(hour)
            print("%d baht" %sol)
        elif 7 <= ans_day <= 365 and ans_day//7 > 3:
            sol = (ans_day*200)-(((ans_day//7)*300)+500)+anshour(hour)
            print("%d baht" %sol)
    else:
        print("error")
main()
