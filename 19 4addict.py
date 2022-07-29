'''4 Addict'''
def main():
    '''main'''
    num = float(input())
    ans = ((((num + 4)**(1/4)) + (num/4))/(4*num - 4))*44
    echo_times = int(num//44)
    text = input()
    print(text*echo_times)
    print("%.4f"%ans)
main()
