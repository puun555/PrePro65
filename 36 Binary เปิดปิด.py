'''binaryปิด/เปิด'''
def main():
    '''main'''
    num = int(input())
    binary = bin(num)[2:]
    if len(binary) == 1:
        print(binary.replace("1", "open").replace("0", "close"))
    else:
        print(binary[0:len(binary)-1].replace("1", "open, ").replace("0", "close, ") + \
            binary[len(binary)-1].replace("1", "open").replace("0", "close"))
main()
