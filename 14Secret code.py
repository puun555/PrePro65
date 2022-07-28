'''Secret code'''
def main():
    '''main'''
    num = int(input())
    print(num%1000000000//100000000, num%10000000//1000000, \
num%100000//10000, num%1000//100, num%10, sep='')
main()
