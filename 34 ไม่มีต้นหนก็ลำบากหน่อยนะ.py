'''ไม่มีต้นหนก็ลำบากหน่อยนะ'''
def main():
    '''main'''
    fish = input()
    count = int(input())
    num = fish.count("<^))))><")
    if num > count:
        print("We have many fish ahoyy!!!")
    elif num == count:
        print("We have enough fish for everyone.")
    elif num * 2 == count:
        print("We can share the fish together Yahoooo!!!")
    else:
        print("No one will eat them  because we cannot be divided the fish.")
main()
