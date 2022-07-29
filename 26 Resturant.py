'''Restaurant'''
def main():
    '''main'''
    age = int(input())
    plate = int(input())
    if age >= 60:
        if plate > 1:
            print("Pay %d baht"%(50*plate))
        else:
            print('Free')
    else:
        print("Pay %d baht"%(100*plate))
main()
