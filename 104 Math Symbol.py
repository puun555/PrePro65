'''math symbol'''
def cal(arrnum, num):
    """calculation"""
    ans = int(arrnum[0])
    if num == '+':
        for i in arrnum[1:]:
            ans += int(i)
    elif num == '-':
        for i in arrnum[1:]:
            ans -= int(i)
    elif num == '*':
        for i in arrnum[1:]:
            ans *= int(i)
    elif num == '/':
        for i in arrnum[1:]:
            ans /= int(i)
    print("%.2f" %ans)
def main():
    '''main'''
    arrnum = []
    while True:
        num = input()
        if num.isnumeric():
            arrnum.append(num)
        else:
            cal(arrnum, num)
            break
main()
