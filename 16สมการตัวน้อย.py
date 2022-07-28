"""สมการตัวน้อย"""
def main():
    """Print สมการตัวน้อย"""
    int_a = int(input())
    int_b = int(input())
    int_c = int(input())
    int_d = int(input())
    int_x = int(input())
    int_y = int(input())
    ans_1 = ((int_b * int_d) / (int_a ** 2)) # ตัวบนตัวแรก
    ans_2 = ans_1 + (int_x * (int_b / int_a)) # ตัวบนแรก + ตัวที่่2
    ans_3 = ans_2 * int_y # mul Y
    ans_4 = ans_3 / (int_y * int_c) # Divided YC
    print("%.2f" %(ans_4))
main()
