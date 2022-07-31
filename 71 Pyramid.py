'''Pyramid'''
def main():
    '''main'''
    num = int(input())
    mirror = num-1
    for i in range(num):
        for j in range(-mirror, mirror+1):
            if abs(j) <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
main()
