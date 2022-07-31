'''นาฬิกาทราย'''
def main():
    '''main'''
    num = int(input())*2 + 1
    mirror = num//2
    print('*'*num)
    for i in range(-mirror, -mirror+num):
        for j in range(-mirror, -mirror+num):
            if abs(j) == abs(i):
                print("*", end='')
            else:
                print(" ", end='')
        print()
    print('*'*num)
main()
