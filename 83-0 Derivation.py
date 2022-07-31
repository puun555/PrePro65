'''Derivative CR:P'เคน'''
def main(arrnum):
    '''main'''
    list_a = arrnum.split(',')
    ans = []
    for i in list_a:
        ans.append(int(i))

    num = len(ans)
    diff = [0]*num
    for i in range(1, num):
        diff[i - 1] = ans[i]*i
    print(diff)
main(input())
