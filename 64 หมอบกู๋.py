'''หมอบกู๋'''
def main():
    '''main'''
    money = float(input())
    min_cost = 0
    shop_count = 0
    shop_buy = 0
    not_get_lunch = True
    while not_get_lunch:
        chaffer_count = 1
        shop_count += 1
        if shop_count == 10:
            not_get_lunch = False
        while chaffer_count <= 5:
            cost = float(input())
            if cost < money:
                min_cost = cost
                shop_buy = shop_count
                not_get_lunch = False
                break
            elif min_cost > cost or min_cost == 0:
                min_cost = cost
                shop_buy = shop_count
            chaffer_count += 1
    print("%.2f"%min_cost)
    print(shop_buy)
main()
