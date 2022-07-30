'''Machine'''
def main():
    '''main'''
    num1 = int(input())
    num2 = int(input())
    intpass = ""
    ans = 0
    if num2 > num1:
        for i in range(num1, num2+1):
            if i%2 != 0:
                intpass += str(i)+" "
                ans += i
    else:
        for i in range(num1+1, num2, -1):
            if i%2 != 0:
                intpass += str(i)+" "
                ans += i
    print("Integer Pass : " + intpass)
    print("Sum Answer : " + str(ans))
main()
