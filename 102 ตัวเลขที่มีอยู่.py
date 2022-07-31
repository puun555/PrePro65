"""Cr. P'เขมฐิติ"""
def main():
    """docstring"""
    last = int(input())
    ans = 0
    if last == 0:
        print("No Tape Measure")
    else:
        while True:
            num = input()
            if num == "No more!":
                break
            else:
                for i in range(1, last+1):
                    if i == int(num):
                        ans += i
        if ans == 0:
            print("Not Found Number")
        else:
            print("Sum of Found Number = %d" %ans)
main()
