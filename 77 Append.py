'''Append'''
def main():
    '''main'''
    num = int(input())
    arr = []
    for _ in range(num):
        arr.append('"%s"'%input())
    print("[" + ", ".join(arr) + "]")
main()
