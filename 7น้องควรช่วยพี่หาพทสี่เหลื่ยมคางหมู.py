'''น้องน้องควรช่วยพี่ หาพื้นที่ของคางหมู'''
def main():
    '''main'''
    height = float(input())
    para1 = float(input())
    para2 = float(input())
    cal = 0.5*height*(para1 + para2) #1/2 * สูง * ผลบวกด้านคู่ขนาน
    print("Trapezoidal area = %.2f"%cal)
main()
