'''Increase'''
def main():
    '''main'''
    ans = 0
    while True:
        num = int(input())
        if num >= 0:
            ans += num
        else:
            break
    print(ans)
main()
