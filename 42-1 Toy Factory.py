'''Toy Factory'''
def factory(num):
    '''factory'''
    if num == 1:
        print(" ^----^")
    elif num == 2:
        print("( 0--0 )")
    elif num == 3:
        print("<------>")
    elif num == 4:
        print("(------)")
    elif num == 5:
        print(" u----u")

def main():
    '''main'''
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    factory(num1)
    factory(num2)
    factory(num3)
    factory(num4)
    factory(num5)
main()
