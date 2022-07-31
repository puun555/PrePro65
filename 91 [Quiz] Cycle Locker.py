'''Cycle Locker'''
def main(num1, num2, total):
    '''main'''
    for i in range(4):
        num_a = int(num1[i])
        num_b = int(num2[i])
        ans = abs(num_a-num_b)
        if ans > 5:
            ans = abs(ans - 10)
        total += ans
    print(total)
main(input(), input(), 0)
