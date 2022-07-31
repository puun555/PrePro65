'''ปิงฉีหลิน'''
def main():
    '''main'''
    num = int(input())*2 - 1
    mirror = num//2
    text1 = input().lower()
    if text1 in "mscbr":
        counter = 1
        for i in range(-mirror, mirror+1):
            for j in range(-mirror, mirror+1):
                if abs(j) <= mirror - abs(i):
                    if counter > mirror+1:
                        print("_", end='')
                    else:
                        print(text1, end='')
                else:
                    print(" ", end='')
            counter += 1
            print()
    else:
        print('Hey!,buy another shop.')
main()
