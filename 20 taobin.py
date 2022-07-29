'''Taobin เต่าบิน'''
def main():
    '''main'''
    money = float(input())
    price = float(input())
    remain = money - price
    mostcoin = remain//0.25
    leastcoin = remain//10 + (remain%10//5) + (remain%5//2) + (remain%2//1) + \
(remain%1//0.5) + (remain%0.5//0.25)
    print(int(mostcoin))
    print(int(leastcoin))
    print("%.1f"%remain)
main()
