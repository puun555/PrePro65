"""[Quiz] เรื่องวุ่นๆกับวัยรุ่นจำนวนเฉพาะ"""
def main(num):
    '''main'''
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")
main(int(input()))
