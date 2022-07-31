'''คณิตศาสตร์เข้าใจยากแต่รักเธอมากเข้าใจไหม CR:P'หมูกรอบ'''
def main():
    '''main'''
    list_a = input().strip('[').strip(']').split(', ')
    list_a = [int(i) for i in list_a]
    print(calcu(list_a))

def calcu(list_a):
    """thonny girl"""
    list_c = []
    for i in range(len(list_a)):
        num = list_a[i]
        for j in range(i-1, -1, -1):
            num = list_a[j] + 1/num
        list_c.append(round(num, 6))
    return list_c
main()
