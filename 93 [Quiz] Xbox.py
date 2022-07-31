"""Xbox CR:P'ทิว"""
def main():
    """https://www.youtube.com/watch?v=tTUml3pcbZY"""
    num = int(input())
    jnum = num*2
    for i in range(1, num+1):
        for j in range(1, jnum):
            ans = " "
            if j == 1 or j == jnum-1 or (i == 1 and j%2 == 1) or (i == num and j%2 == 1):
                ans = "*"
            if i+j == 2+(3*(i-1)) or i+j == jnum-i+1:
                ans = "*"
            print(ans, end="")
        print()
main()
