'''คู่อันดับ'''
def main():
    '''main'''
    num = int(input())
    for i in range(-num, num+1):
        for j in range(-num, num+1):
            print("(%02d, %02d)"%(abs(i), abs(j)), end=" ")
        print()
main()
