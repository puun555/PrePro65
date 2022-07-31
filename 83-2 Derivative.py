"""Derivative CR:นายธีระรัตน์ สุดสงวน"""
def main(num):
    """loop and print"""
    ans = []
    for i in range(1, len(num)):
        ans.append(int(num[i])*i)
    ans.append(0)
    print(ans)
main(input().split(","))
