'''oh my matrix'''
def main():
    '''main'''
    ma1 = int(input())
    ma2 = int(input())
    ma3 = int(input())
    ma4 = int(input())
    mc1 = int(input())
    mc2 = int(input())
    mc3 = int(input())
    mc4 = int(input())

    mb1 = mc1 - ma1
    mb2 = mc2 - ma2
    mb3 = mc3 - ma3
    mb4 = mc4 - ma4

    sumdet = (-(ma3*ma2) + (ma1*ma4)) + (-(mb3*mb2) + (mb1*mb4)) + (-(mc3*mc2) + (mc1*mc4))

    print("b1: %d"%mb1)
    print("b2: %d"%mb2)
    print("b3: %d"%mb3)
    print("b4: %d"%mb4)
    print("D: %.2f"%sumdet)
main()
