'''อักษรที่หายไป'''
def main():
    '''main'''
    text = input()
    if "\"" in text:
        text = text.split("\"")
        text[1] = (chr(int(text[1])))
        print("".join(text))
    else:
        print("No error")
main()
