'''Choose a book'''
import math
def main():
    '''main'''
    num1 = int(input())
    num2 = int(input())
    cal = math.factorial(num1)/(math.factorial(num2)*math.factorial(num1 - num2))
    print(int(cal))
main()
