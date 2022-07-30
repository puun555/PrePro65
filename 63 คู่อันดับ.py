'''คู่อันดับแบบตามใจฉัน'''
def main():
    '''main'''
    num1 = int(input())
    num2 = int(input())
    for i in range(num1):
        for j in range(num2):
            print("(%d, %d)"%(i+1, j+1), end=" ")
        print()
main()
