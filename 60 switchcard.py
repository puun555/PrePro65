""" ลองสลับการ์ด แล้วตัดขาดจากใจเธออีกครั้ง CR:นายธนพล นิ่มนวล """

def main(lap):
    """prepro"""
    pos1, pos2, pos3 = "A", "B", "C"
    for _ in range(lap):
        shuf = input()
        if shuf in "1221":
            pos1, pos2 = pos2, pos1
        elif shuf in "2332":
            pos2, pos3 = pos3, pos2
        elif shuf in "3113":
            pos1, pos3 = pos3, pos1
    print("%s\n%s\n%s" %(pos1, pos2, pos3))
main(int(input()))
