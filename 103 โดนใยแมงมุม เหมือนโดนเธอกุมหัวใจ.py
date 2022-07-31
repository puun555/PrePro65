'''main'''
def main():
    '''main'''
    num = int(input())
    for i in range(-num, num+1):
        for j in range(-num, num+1):
            con1 = abs(j) == 0 or abs(i) == 0 or abs(j) == abs(i)
            con2 = abs(i)%2 != 0 and abs(j) <= abs(i)
            con3 = abs(j)%2 != 0 and abs(i) <= abs(j)
            if con1 or con2 or con3:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()
main()
