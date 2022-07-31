'''Walking average distance'''
import math
def main():
    '''main'''
    days = int(input())
    arr_step = []
    for _ in range(days):
        arr_step.append(int(input()))
    avg = (sum(arr_step)/days)
    for i in arr_step:
        print(math.ceil(abs(i - avg)))
main()
