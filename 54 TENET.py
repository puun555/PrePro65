'''TENET'''
def main():
    '''main'''
    num = int(input())
    for _ in range(num):
        text = input()
        if text == text[::-1]:
            print(text)
main()
