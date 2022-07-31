'''บันไดแมว'''
def main():
    '''main'''
    num = int(input())
    for i in range(num):
        for j in range(num):
            if i >= j+1:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()
main()
