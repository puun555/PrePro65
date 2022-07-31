'''[Quiz] Nintendo Battery'''
def main():
    '''main'''
    percentage = int(input())
    fullbattery = int(input())
    remain = int(fullbattery*(percentage/100))
    print("(%s%s) %d%%"%(remain*"O", (fullbattery-remain)*"_", percentage))
main()
