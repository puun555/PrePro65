'''Chocolate cake'''
def main():
    '''main'''
    money = int(input())
    price = int(input())
    cake = money//price
    remain = money%price
    if cake <= 0:
        print("Not enough money;(")
        print("Money left: %d"%remain)
    else:
        print("Chocolate Cake: %d"%cake)
        print("Money left: %d"%remain)
main()
