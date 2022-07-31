'''Diamond'''
def main():
    '''main'''
    num = int(input())
    mirror = num//2
    for i in range(-mirror, -mirror+num):
        for j in range(-mirror, -mirror+num):
            con = abs(j) <= 0 + abs(abs(i) - mirror) or i == mirror + 1
            if con:
                print("*", end='')
            else:
                print(" ", end='')
        print()
main()
