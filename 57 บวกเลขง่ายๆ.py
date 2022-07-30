'''บวกเลขง่ายๆ'''
def main(ans):
    '''main'''
    # ans = 0
    for _ in range(10):
        num = int(input())
        if num >= 0:
            ans += num
        else:
            ans += -5
    print(ans*(ans >= 0) + -5*(ans < 0))
main(0)
