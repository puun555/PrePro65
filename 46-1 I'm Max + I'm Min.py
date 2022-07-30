"""I'm Max & I'm Min"""
def main():
    """หา ค่าที่มากที่สุดหรือค่าที่น้อยที่สุด จากเลขจำนวนเต็มทั้งหมด 5 จำนวน"""
    more = input().upper()
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    if more == "MAX":
        findx(num1, num2, num3, num4, num5)
    elif more == "MIN":
        findn(num1, num2, num3, num4, num5)
def comparex(xan, yon):
    """เทียบตัวมากสุด"""
    if xan > yon:
        return xan
    else:
        return yon
def comparen(xan, yon):
    """เทียบตัวน้อยสุด"""
    if xan > yon:
        return yon
    else:
        return xan
def findx(ant, bird, cat, dog, egg):
    """หาตัวมากสุด"""
    fog = comparex(ant, bird)
    gon = comparex(fog, cat)
    hot = comparex(gon, dog)
    kin = comparex(hot, egg)
    print("MAX : " + str(kin))
def findn(ant, bird, cat, dog, egg):
    """หาตัวน้อยสุด"""
    fog = comparen(ant, bird)
    gon = comparen(fog, cat)
    hot = comparen(gon, dog)
    kin = comparen(hot, egg)
    print("MIN : " + str(kin))
main()
