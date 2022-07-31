'''คณิตพาเพลิน'''
def main():
    '''main'''
    num_times = int(input())
    arr_num = []
    arr_mul = []
    for _ in range(num_times):
        arr_num.append(int(input()))
    multiplier = float(input())
    for i in arr_num:
        arr_mul.append(str(format(i*multiplier, '.2f')))
    print(arr_mul)
main()
