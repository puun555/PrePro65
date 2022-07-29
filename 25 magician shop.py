'''Magiciam suit shop'''
def fairytales(num):
    '''fairytales'''
    print("Total %d Jewel"%((12800*num)*0.8))

def sabertooth(num):
    '''sabertooth'''
    if num > 5:
        print("Total %d Jewel"%((12800*num)*0.85))
    else:
        print("Total %d Jewel"%(12800*num))

def lamia(num):
    '''lamia'''
    if num >= 3:
        print("Total %d Jewel"%((12800*num)*0.90))
    else:
        print("Total %d Jewel"%(12800*num))

def bluepeg(num):
    '''bluepeg'''
    if num > 10:
        print("Total %d Jewel"%((12800*num)*0.95))
    else:
        print("Total %d Jewel"%(12800*num))

def main():
    '''main'''
    job = input()
    if job == "Magician":
        guild = input()
        num = int(input())
        if guild == 'Fairy Tail':
            fairytales(num)
        elif guild == 'Sabertooth':
            sabertooth(num)
        elif guild == 'Lamia Scale':
            lamia(num)
        elif guild == 'Blue Pegasus':
            bluepeg(num)
        else:
            print("Total %d Jewel"%(12800*num))
    else:
        num = int(input())
        print("Total %d Jewel"%(12800*num))
main()
