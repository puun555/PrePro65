'''Yes Or No'''
def main():
    '''main'''
    text = input().isalnum()
    print(text*"Yes, it is." + (text == 0)*"No, it's not.")
main()
