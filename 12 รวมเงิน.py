'''รวมเงิน'''
def main():
    '''main'''
    name1 = input()
    name2 = input()
    money1 = float(input())
    money2 = float(input())
    section = input()
    sep1 = input()
    print("%s %s"%(name1, name2), money1 + money2, section, sep=sep1)
main()
