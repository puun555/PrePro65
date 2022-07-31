"""Cr. P'pan"""
def main():
    """เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
    i_have = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    money_left = i_have - water
    if money_left % 3 == 0:
        price_snack1 = 10 * snack1
    elif money_left % 3 == 1:
        price_snack1 = 15 * snack1
    elif money_left % 3 == 2:
        price_snack1 = 20 * snack1
    money_left = money_left - price_snack1
    if money_left % 3 == 0:
        price_snack2 = 12 * snack2
    elif money_left % 3 == 1:
        price_snack2 = 15 * snack2
    elif money_left % 3 == 2:
        price_snack2 = 18 * snack2
    money_left = money_left - price_snack2
    if money_left % 3 == 0:
        price_snack3 = 5 * snack3
    elif money_left % 3 == 1:
        price_snack3 = 7 * snack3
    elif money_left % 3 == 2:
        price_snack3 = 9 * snack3
    money_left = money_left - price_snack3
    if money_left < 0:
        print("Now you have %d left." %i_have)
        print("You don't have enough money!")
    else:
        print("Now you have %d left." %money_left)
        print("Here's your order!")
        print("Water: %d baht" %water)
        print("Snack number 1: %d baht" %price_snack1)
        print("Snack number 2: %d baht" %price_snack2)
        print("Snack number 3: %d baht" %price_snack3)
main()