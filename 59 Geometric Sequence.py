"""Geometric Sequence CR:นายตรัยธรรม แสงเดือน"""
def main():
    """Geometric Sequence"""
    num1 = float(input())
    num2 = int(input())
    num3 = float(input())
    plao = ""
    for _ in range(num2):
        plao = plao + str("%.2f"%(num1)) + " "
        num1 *= num3
    print(plao)
main()
