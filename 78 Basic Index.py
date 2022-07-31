'''Basic Index'''
def main():
    '''main'''
    arr = []
    while True:
        char = input()
        if char.upper() == "END":
            break
        arr.append(char)
    num = int(input())
    if num <= len(arr) - 1:
        print('List[%d] = "%s"'%(num, arr[num]))
    else:
        print('Index Not Found')
main()
