'''Pager'''
def main():
    '''main'''
    lenght_text = len(input())
    print('Text\'s length is : "%d"'%lenght_text)
    price1 = lenght_text//20
    lenght_text %= 20
    price2 = lenght_text//8
    lenght_text %= 8
    price3 = lenght_text//3
    lenght_text %= 3
    price4 = lenght_text//1
    lenght_text %= 1
    price = price1*18.5 + price2*6.5 + price3*3 + price4*1.5
    print("Total price is   : %.2f Baht\\.-"%price)
main()
