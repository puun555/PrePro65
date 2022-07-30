"""Show me the money CR:P'ธนพล นิ่มนวล"""

def main(pay, cost):
    """Show me the money"""
    ton = pay - cost
    if ton < 0:
        print("จำนวนเงินไม่พอ")
    elif ton == 0:
        print("จ่ายมาพอดี")
    else:
        print("เเบงค์ 100 บาท : %d" %(ton // 100))
        print("เเบงค์ 50 บาท : %d" %(ton % 100 // 50))
        print("เเบงค์ 20 บาท : %d" %(ton % 50 // 20))
        print("เหรียญ 12 บาท : %d" %(ton % 20 // 12))
        print("เหรียญ 10 บาท : %d" %(ton % 12 // 10))
        print("เหรียญ 5 บาท : %d" %(ton % 10 // 5))
        print("เหรียญ 2 บาท : %d" %(ton % 100 % 50 % 20 % 12 % 10 % 5// 2))
        print("เหรียญ 1 บาท : %d" %(ton % 2 // 1))
        print("เหรียญ 50 สตางค์ : %d" %(ton % 1 // 0.5))
        print("เหรียญ 25 สตางค์ : %d" %(ton % 0.5 // 0.25))
main(float(input()), float(input()))
