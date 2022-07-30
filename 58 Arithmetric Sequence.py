'''	Arithmetic Sequence'''
def main():
    '''main'''
    num1 = int(input())
    member = int(input())
    numd = int(input())
    numn = num1 + (member - 1)*numd

    if numd != 0:
        for i in range(num1, ((numn >= 0)*(numn+1)) + ((numn < 0)*(numn-1)), numd):
            print(i, end=' ')
    else:
        for _ in range(member):
            print(num1, end=' ')
main()
