'''คณิตศาสตร์เข้าใจยากแต่รักเธอมากเข้าใจไหม CR:นายจารุกิตติ์ ศรีพาเพลิน'''
def main():
    '''main'''
    def quick_maff(listof):
        '''But recursion is hard'''
        if len(listof) == 1:
            return listof[0]
        return listof[0] + (1/quick_maff(listof[1:len(listof)]))
    result = []
    list_of_a = input().strip("[] ").split(",")
    list_of_a = [int(i) for i in list_of_a]
    for i in range(len(list_of_a)):
        result.append(round(quick_maff(list_of_a[0:i+1]), 6))
    print(result)
main()
