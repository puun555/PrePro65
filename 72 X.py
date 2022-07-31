'''X'''
def main():
    '''main'''
    num = int(input())
    mirror = num//2
    for i in range(-mirror, -mirror+num):
        for j in range(-mirror, -mirror+num):
            if abs(j) == abs(i):
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()
main()
