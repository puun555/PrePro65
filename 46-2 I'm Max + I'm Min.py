"""I'm Max I'm Min"""
def main():
    """Min Max"""
    method = input().casefold()
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    if method == "max":
        result = ax_num(ax_num(ax_num(ax_num(num1, num2), num3), num4), num5)
        print("MAX : %d" %result)
    elif method == "min":
        result = in_num(in_num(in_num(in_num(num1, num2), num3), num4), num5)
        print("MIN : %d" %result)
def ax_num(num1, num2):
    """max calculation"""
    return ((num1 + num2) + abs(num1 - num2)) / 2
def in_num(num1, num2):
    """mix calculation"""
    if ((num1 + num2) + abs(num1 - num2)) / 2 == num1:
        return num2
    elif ((num1 + num2) + abs(num1 - num2)) / 2 == num2:
        return num1
    else:
        return num1
main()
