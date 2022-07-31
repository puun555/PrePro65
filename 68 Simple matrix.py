'''Simple matrix'''
def main():
    '''main'''
    num1 = int(input())
    num2 = int(input())
    for i in range(num1):
        for j in range(num2):
            print((j+1)*(i+1), end=" ")
        print()
main()
