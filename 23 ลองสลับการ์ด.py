'''switch card ลองสลับการ์ด แล้วตัดขาดจากใจเธอ'''
def main():
    '''main'''
    pos = input()
    if pos == '12' or pos == '21':
        print("A")
    elif pos == "32" or pos == "23":
        print("C")
    else:
        print("B")
main()
