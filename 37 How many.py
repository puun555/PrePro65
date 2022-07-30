'''How Many'''
def main():
    '''main'''
    text = input().casefold()
    word = input().casefold()
    num = text.count(word)
    if len(word) == 1 and num != 0:
        print("Character :", num)
    elif len(word) > 1 and num != 0:
        print("Word :", num)
    else:
        print("No word and character.")
main()
