"""[Extra] ถอดรหัสเปลี่ยนโลก CR:P'ปุญญพันธ์ ทิพย์"""
def main():
    """doc"""
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    txt = input().upper()
    kuu = [input().upper(), input().upper(), input().upper()]
    temp = []
    ans = ""
    num = 0
    for i in kuu:
        temp += [(alph.index(i[0])+alph.index(i[1]))%26]
    for i in txt:
        if i in alph:
            ans += alph[(alph.index(i)-temp[num//3%3])%26]
            num += 1
        else:
            ans += i
    print(ans.capitalize())
main()
