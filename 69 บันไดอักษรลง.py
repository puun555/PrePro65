'''บันไดอักษรลง'''
def main():
    '''main'''
    num1 = ord(input().upper()) - 65
    for i in range(num1+1):
        for j in range(i+1):
            print(chr(65+j), end=' ')
        print()
main()
