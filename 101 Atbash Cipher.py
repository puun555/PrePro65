"""Cr. P'ชญานนท์"""
def main():
    """ Input then print """
    text = input()
    for character in text:
        if character.isupper():
            print(chr(65 - ord(character)+90), end="")
        elif character.islower():
            print(chr(97 - ord(character)+122), end="")
        else:
            print(character, end="")
main()
